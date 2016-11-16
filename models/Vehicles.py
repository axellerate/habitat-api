from BaseModel import *
from CarsModel import CarsModel
from MotorcyclesModel import MotorcyclesModel
from PublicTransitModel import PublicTransitModel
from ZeroEmissionsTransportModel import ZeroEmissionsTransportModel

class Vehicles(BaseModel):

	self.possible_types = ['car', 'motorcycle', 'public_transit',
												'zero_emissions_transport']

	car = KeyProperty(kind = "Cars")
	motorcycle = KeyProperty(kind = "Motorcycles")
	zero_emissions_transport = KeyProperty(kind = "ZeroEmissionsTransport")
	public_transit = KeyProperty(kind = "PublicTransitModel")
	vehicle_type = StringProperty(required = True)

	def add_vehicle(cls, vehicle_dict):
		if vehicle_dict['type'] not in self.possible_types:
			return None
		if vehicle_dict['type'] == "car":
			self.add_car(vehicle_dict)
		elif vehicle_dict['type'] == "motorcycle":
			self.add_motorcycle(vehicle_dict)
		elif vehicle_dict['type'] == "public_transit":
			self.add_public_transit(vehicle_dict)
		elif vehicle_dict['type'] == "zero_emissions_transport":
			self.add_zero_emissions_transport(vehicle_dict)
		else:
			return None
	
	def add_car(self, vehicle_dict):
		car = CarsModel.add_vehicle(vehicle_dict)
		self.car = car.key
		self.vehicle_type = "car"
		return True
	
	def add_motorcycle(self):
		motorcycle = MotorcyclesModel.add_vehicle(vehicle_dict)
		self.motorcycle = motorcycle.key
		self.vehicle_type = "motorcycle"
		return True
	
	def add_public_transit(self):
		public_transit = PublicTransitModel.add_vehicle(vehicle_dict)
		self.public_transit = public_transit.key
		self.vehicle_type = "public_transit"
		return True

	def add_zero_emissions_transport(self):
		z_e_t = ZeroEmissionsTransportModel.add_vehicle(vehicle_dict)
		self.zero_emissions_transport = z_e_t.key
		self.vehicle_type = "zero_emissions_transport"
		return True