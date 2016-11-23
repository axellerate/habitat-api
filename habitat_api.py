from google.appengine.ext import endpoints

from api_endpoints.vehicles_api import *
from api_endpoints.distances_emissions_api import *
from api_endpoints.users_api import *

APPLICATION = endpoints.api_server([VehiclesAPI,DistancesEmissionsAPI,UsersAPI],
										restricted=False)