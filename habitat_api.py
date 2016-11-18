from google.appengine.ext import endpoints

from api_endpoints.vehicles_api import *

APPLICATION = endpoints.api_server([VehiclesAPI],
										restricted=False)