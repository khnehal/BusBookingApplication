# import re
# from django.db.models import Q
from django.shortcuts import render
from rest_framework import (
    generics,
    status
)
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    Location,
    Schedule
)
from .serializers import (
    LocationSerializer,
    ScheduleSerializer
)
from .utils import (
    parse_date
)


def index(request):
    return render(request, 'booking/search_results.html')


class LocationListAPIView(generics.ListAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


# Generics not used here as post does not create an object
# Hence using generics may be against the standards
class ScheduleSearchAPIView(APIView):

    def post(self, request, format=None):
        request_data = request.data
        if (
            'from_location' not in request_data or
            not request_data['from_location'] or
            'to_location' not in request_data or
            not request_data['to_location'] or
            'onward_date' not in request_data or
            not request_data['onward_date']
        ):
            return Response(
                "Invalid Request. Please ensure from_location, to_location " +
                "and onward_date are present in the request",
                status=status.HTTP_400_BAD_REQUEST
            )
        # Retrieve journey start date schedule list
        filter_dict_onward = {
            'from_location__name': request_data['from_location'],
            'to_location__name': request_data['to_location'],
            'departure_time__contains': parse_date(request_data['onward_date'])
        }
        schedules_onward_objects = Schedule.objects.filter(**filter_dict_onward)
        schedules_onward_data = ScheduleSerializer(schedules_onward_objects, many=True).data
        result = {
            'schedules_onward': schedules_onward_data,
            'schedules_return': []
        }

        # Retrieve journey end date schedule list if return date is present
        if request_data.get('return_date', None):
            filter_dict_return = {
                'from_location__name': request_data['to_location'],
                'to_location__name': request_data['from_location'],
                'arrival_time__contains': parse_date(request_data['return_date'])
            }
            schedules_return_objects = Schedule.objects.filter(**filter_dict_return)
            schedules_return_data = ScheduleSerializer(schedules_return_objects, many=True).data
            result['schedules_return'] = schedules_return_data

        return Response(result)
