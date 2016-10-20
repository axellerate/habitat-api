from google.appengine.ext import endpoints
from google.appengine.ext import ndb

from habitat_api_messages import *



class BaseModel(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add = True)
	updated = ndb.DateTimeProperty(auto_now = True)


class User(BaseModel):

	"""
	Contains the User data from Google
	"""

	google_user_id = ndb.StringProperty(required = True)

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


class Cars(BaseModel):

	"""
	Stores the car data from http://www.FuelEconomy.gov
	"""

	car_id = ndb.IntegerProperty(required = True)
	make = ndb.StringProperty(required = True)
	model = ndb.StringProperty(required = True)
	year = ndb.IntegerProperty(required = True)
	emissions_per_mile = ndb.FloatProperty(required = True)

	@property
	def emissions_per_km(self):
		return (self.emissions_per_mile / 1.67)

	def to_message(self):
		return CarMessage(car_id=self.car_id,
							make=self.make,
							model=self.model,
							year=self.year,
							emissions_per_mile=self.emissions_per_mile)

	@classmethod
	def addNewCar(cls, car):
		newCar = cls()
		newCar.car_id = car.car_id
		newCar.make = car.make
		newCar.model = car.model
		newCar.year = car.year
		newCar.emissions_per_mile = car.emissions_per_mile
		newCar.put()
		return newCar


class Emissions(BaseModel):

	"""
	Stores the emissions data
	"""

	distance = ndb.KeyProperty(kind = "Distances")
	transport = ndb.KeyProperty(kind = "Transportation")
	emissions = ndb.FloatProperty(default = 0)

class Distances(BaseModel):

	"""
	Contains emissions data from each user.
	Emissions can be calcluated on the fly 
	from this table
	"""

	user = ndb.KeyProperty(kind = "Users")
	distance = ndb.IntegerProperty(default = 0)
