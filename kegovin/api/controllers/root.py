
from pecan import rest
from wsme import types as wtypes

from kegovin.api.controllers.v1 import controller as v1_controller
from kegovin.api import expose


class RootController(rest.RestController):
    v1 = v1_controller.V1Controller()

    @expose.expose(wtypes.text)
    def get(self):
        return "webdemo"
