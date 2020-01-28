from datetime import date 
from sanic_openapi import doc 

class Manufacturer:
    name = str
    start_date = date

class Driver:
    name = str
    birthday = date