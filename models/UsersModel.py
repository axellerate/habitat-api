from BaseModel import *

class UsersModel(BaseModel):

	"""
	Contains the User data from Google
	"""
	google_user_id = ndb.StringProperty(required = True)
	primary_vehicle = ndb.KeyProperty(kind = "Vehicle")
	secondary_vehicle = ndb.KeyProperty(kind = "Vehicle")
	city = ndb.StringProperty()
	country = ndb.StringProperty()


	@classmethod
	def add_user(cls, user_id):
		user_exists = cls.query(cls.google_user_id == user_id).get()
		if not user_exists:
			new_user = cls(google_user_id = user_id)
			key = new_user.put()
			return key
		return user_exists

	@classmethod
	def get_user_by_id(cls, user_id):
		user = cls.query(cls.google_user_id == user_id).get()
		if user: 
			return user
		else:
			return None