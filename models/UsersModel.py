from BaseModel import *

class Users(BaseModel):

	"""
	Contains the User data from Google
	"""

	google_user = ndb.UserProperty(required = True)
	primary_vehicle = ndb.KeyProperty(kind = "Vehicle")
	secondary_vehicle = ndb.KeyProperty(kind = "Vehicle")