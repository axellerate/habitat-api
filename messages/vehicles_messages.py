from protorpc import messages
from cars_messages import *

class VehicleMessage(messages.Message):
	car = messages.MessageField(CarMessage, 1)
	# motorcycle = MessageField(MotorcycleMessage, 2)
	# zero_emissions_vehicle = MessageField(ZeroEmissionsVehicleMessage, 3)
	# public_transit = MessageField(PublicTransitMessage, 4)
	message = messages.StringField(2)

class VehiclesMessage(messages.Message):
	vehicle_type = messages.StringField(1)
	vehicles_count = messages.IntegerField(2)
	vehicles = messages.MessageField(VehicleMessage, 3, repeated=True)
	# motorcycle = MessageField(MotorcycleMessage, 2)
	# zero_emissions_vehicle = MessageField(ZeroEmissionsVehicleMessage, 3)
	# public_transit = MessageField(PublicTransitMessage, 4)
	message = messages.StringField(4)

class VehicleTypeIdMessage(messages.Message):
	vehicle_id = messages.IntegerField(1)
	vehicle_type = messages.StringField(2)
