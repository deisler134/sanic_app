from sanic.views import HTTPMethodView
from sanic.blueprints import Blueprint
from sanic.response import json
from sanic_openapi import doc

blueprint = Blueprint('Repair', '/repair')
from api.models import Station
from test.test_data import test_station


class RepairStation(HTTPMethodView):
    @doc.summary("Fetches all repair stations")
    @doc.produces([Station])
    def get(self, request):
        return json([test_station])

    @doc.summary("make an appointment")
    @doc.description("submit necessary information for appointment")
    def post(self, request):
        return json(request.json)


blueprint.add_route(RepairStation.as_view(), "/station", strict_slashes=True)