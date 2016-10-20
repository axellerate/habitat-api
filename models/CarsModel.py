from BaseModel import *
from messages.cars_messages import *

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
