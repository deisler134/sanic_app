from api.models import Manufacturer, Driver
import datetime

test_manufacturer = Manufacturer()
test_driver = Driver()

test_manufacturer = {
    'id' : 1,
    'name' : 'Nissan',
    'start_date' : str(datetime.date(year=1933,month=12,day=26))
}

test_driver = {
    'id' : 1,
    'name' : 'Sanic',
    'birthday' : str(datetime.date(year=2020,month=1,day=5))
}

test_car = {
    'id': 1,
    'on': False,
    'doors': 2,
    'color': 'black',
    'make': test_manufacturer,
    'passengers': [test_driver]
}

test_garage = {
    'spaces': 2,
    'cars': [test_car]
}

test_success = {
    'success': True
}

test_station = {
    'contact': 00000000,
    'location': 'Seattle',
}