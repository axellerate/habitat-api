from BaseModel import *

class Transportation(BaseModel):

	"""
	Contains the Transportation info for each user.
	"""

	user = ndb.KeyProperty(kind = "Users")
	primary = ndb.StringProperty(required = True)
	secondary = ndb.StringProperty(required = True)
	cars = ndb.KeyProperty(repeated = True, kind = "Cars")

	def set_primary(self, mode):
		possible_types = ["car", "walking", 
			"biking", "public_transit", "electric"]
		if mode in possible_types:
			this.primary = mode
			return mode
		return None

	@classmethod
	def get_modes(cls):
		return ["car", "walking", 
			"biking", "public_transit", "electric"]