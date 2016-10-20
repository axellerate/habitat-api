from BaseModel import *

class Users(BaseModel):

	"""
	Contains the User data from Google
	"""

	google_user_id = ndb.StringProperty(required = True)