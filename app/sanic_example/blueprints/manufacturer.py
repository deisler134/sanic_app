from sanic.blueprints import Blueprint
from sanic.response import json
from sanic_openapi import doc

from api.models import Driver
from test.test_data import test_manufacturer

blueprint = Blueprint('Manufacturer', '/manufacturer')

@blueprint.get("/", strict_slashes=True)
@doc.summary("Fetches all manufacturers")
@doc.produces([Driver])
async def manufacturer_list(request):
    return json([test_manufacturer])

@blueprint.get("/<manufacturer_id:int>", strict_slashes=True)
@doc.summary("Fetches a manufacturer")
@doc.produces(Driver)
async def manufacturer_get(request, manufacturer_id):
    return json(test_manufacturer)

@blueprint.put("/<manufacturer_id:int>", strict_slashes=True)
@doc.summary("Updates a manufacturer")
@doc.consumes(Driver)
@doc.produces(Driver)
async def manufacturer_put(request, manufacturer_id):
    return json(test_manufacturer)