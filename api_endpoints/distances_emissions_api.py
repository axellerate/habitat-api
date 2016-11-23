from google.appengine.ext import endpoints

from protorpc import message_types
from protorpc import remote

from models.DistancesEmissionsModel import DistancesEmissionsModel
from messages.distances_emissions_messages import *

@endpoints.api(name='distances_emissions', version='v1',
				description='Distances and Emissions API')
class DistancesEmissionsAPI(remote.Service):
	"""Class which defines Distances and Emissions API v1."""

	pass