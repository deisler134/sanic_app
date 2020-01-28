from sanic.blueprints import Blueprint
from sanic.response import json
from sanic_openapi import doc

from api.models import Driver, Status
from test.test_data import test_driver, test_success


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

@blueprint.delete("/<driver_id:int>", strict_slashes=True)
@doc.summary("Deletes a driver")
@doc.produces(Status)
async def driver_delete(request, driver_id):
    return json(test_success)