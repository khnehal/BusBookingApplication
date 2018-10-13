# BusBookingApplication


This Application requires `Python3 and Pip3`


Python 3 can be downloaded from https://www.python.org/downloads/. if you are using python 3.4 or higher, pip3 is already installed. Otherwise download and install manually from https://pip.pypa.io/en/stable/installing/.


Use of virtual environment is recommended. https://virtualenvwrapper.readthedocs.io/en/latest/install.html.


### Download
```
git clone https://github.com/saqlainsyed007/BusBookingApplication.git

cd BusBookingApplication/BusBooking/
```

### Install
```
virtualenv -p python3 busbooking

source busbooking/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runscript seed_data
```

Seed data creates dummy schedules from today to three days from today.


### Run Application
```
python manage.py runserver 0:8000
```

### View Application
Go to `http://localhost:8000/booking/` and search for some buses. A `DummyLocation` is added to view the empty results state.


Go to `http://localhost:8000/admin/` and login with username `admin` and password `changeme` to view all objects that have been created and validate results in the UI.


**Note**: 


Some features may not work in Internet Explorer and Microsoft Edge.

CDNs do not load sometimes. Please hard refresh untill all CDNs are loaded and there are no 403, 404 errors in the browser console
