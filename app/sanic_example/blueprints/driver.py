from sanic.blueprints import Blueprint
from sanic.response import json
from sanic_openapi import doc

from api.models import Driver
from test.test_data import test_driver
# import json

blueprint = Blueprint('Driver', '/driver')

@blueprint.get("/", strict_slashes=True)
@doc.summary("Fetches all drivers")
@doc.produces([Driver])
async def driver_list(request):
    return json([test_driver])


@blueprint.get("/<driver_id:int>", strict_slashes=True)
@doc.summary("Fetches a driver")
@doc.produces(Driver)
async def driver_get(request, driver_id):
    return json(test_driver)


@blueprint.put("/<driver_id:int>", strict_slashes=True)
@doc.summary("Updates a driver")
@doc.consumes(Driver)
@doc.produces(Driver)
async def driver_put(request, driver_id):
    return json(test_driver)