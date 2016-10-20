from protorpc import messages

class CarMessage(messages.Message):

	"""Message for a full Car object"""

	car_id = messages.IntegerField(1, required=True)
	make = messages.StringField(2, required=True)
	model = messages.StringField(3, required=True)
	year = messages.IntegerField(4, required=True)
	emissions_per_mile = messages.FloatField(5, required=True)


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