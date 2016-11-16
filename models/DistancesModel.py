from BaseModel import *

class Distances(BaseModel):

	"""
	Contains emissions data from each user.
	Emissions can be calcluated on the fly 
	from this table
	"""

	user = ndb.KeyProperty(kind = "Users")
	distance = ndb.FloatProperty(default = 0.0)
	start_datetime = ndb.DateTime(required = True)
	end_datetime = ndb.DateTime(required = True)
	vehicle = ndb.KeyProperty(kind = "Vehicle")
	emissions = ndb.FloatProperty(required = True)

	def add_emissions_for_user(self, user, emissions_dict):
		""""
			user = UsersModel object
			emissions_dict = [distance (km), start, end, 
											 vehicle, emissions]
		"""

		pass