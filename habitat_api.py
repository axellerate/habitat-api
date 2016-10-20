from google.appengine.ext import endpoints

from cars_api import *



APPLICATION = endpoints.api_server([CarsAPI],
										restricted=False)