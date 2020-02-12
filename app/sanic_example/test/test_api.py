from ..api.models import Manufacturer, Driver
import datetime
import pytest

def test_Manufacture():
    test_Manufacture = Manufacturer()
    test_manufacturer = {
        'id' : 1,
        'name' : 'Nissan',
        'start_date' : str(datetime.date(year=1933,month=12,day=26))
    }

    assert test_Manufacture.name is str
    assert test_Manufacture.start_date is datetime.date

def check():
    return 'pytest is good'

def test_func():
    assert check() == "pytest is good"