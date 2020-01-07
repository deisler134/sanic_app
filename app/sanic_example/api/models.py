from datetime import date 
from sanic_openapi import doc 

class Manufacturer:
    name = str
    start_date = str

class Driver:
    name : str
    birthday : str