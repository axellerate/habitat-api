from google.appengine.ext import endpoints

from api_endpoints.cars_api import *



APPLICATION = endpoints.api_server([CarsAPI],
										restricted=False)