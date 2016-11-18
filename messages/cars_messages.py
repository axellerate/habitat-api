from protorpc import messages
from protorpc import message_types

class CarMessage(messages.Message):

	"""Message for a full Car object"""

	car_id = messages.IntegerField(1)
	make = messages.StringField(2)
	model = messages.StringField(3)
	year = messages.IntegerField(4)
	co2_grams_per_km = messages.FloatField(5)
	message = messages.StringField(6)
	created = message_types.DateTimeField(7)


class CarsMessage(messages.Message):
	
	"""Message for All Car objects"""

	cars = messages.MessageField(CarMessage, 1, repeated=True)


class CarAddMessage(messages.Message):
	"""
		Message used to Add new Car.
		The id is used to fetch data from
		FuelEconomy.gov - see endpoint handler.
	"""

	car_id = messages.StringField(1, required=True)