from google.appengine.ext import endpoints

from xml.dom import minidom
import urllib

from protorpc import message_types
from protorpc import remote

from models.CarsModel import CarsModel as CarsModel
from messages.cars_messages import *
from messages.vehicles_messages import *

@endpoints.api(name='vehicles', version='v1',
				description='Vehicles API')
class VehiclesAPI(remote.Service):
	"""Class which defines Vehicles API v1."""

	@endpoints.method(VehicleTypeIdMessage, VehicleMessage,
						path='vehicles', http_method='POST',
						name='add')
	def add_vehicle(self, request):
		if request.vehicle_type == "car":
			new_vehicle = CarsModel.add_vehicle(request.vehicle_id)
			if new_vehicle:

				car_message = CarMessage(car_id = new_vehicle.car_id, make = new_vehicle.make,
					model = new_vehicle.model, year = new_vehicle.year, 
					co2_grams_per_km = new_vehicle.co2_grams_per_km,
					created = new_vehicle.created)
			
				return VehicleMessage(car = car_message)
		else:
			return VehicleMessage(message = "Invalid vehicle_type")

	@endpoints.method(VehicleTypeIdMessage, VehiclesMessage,
						path='vehicles', http_method='GET',
						name='get_all_by_type')
	def get_vehicles(self, request):
		if request.vehicle_type == "car":
			cars = CarsModel.get_vehicles()
			all_car_messages = []
			for car in cars:
				car_message = CarMessage(car_id = car.car_id, make = car.make,
					model = car.model, year = car.year, 
					co2_grams_per_km = car.co2_grams_per_km,
					created = car.created)
				all_car_messages.append(car_message)
			all_cars = [VehicleMessage(car = car_message) for car_message in all_car_messages]
        	return VehiclesMessage(vehicles = all_cars, vehicles_count = len(all_cars),
								   vehicle_type = request.vehicle_type)

	@endpoints.method(VehicleTypeIdMessage, VehicleMessage,
						path='vehicle', http_method='GET',
						name='get_by_id')
	def get_vehicle(self, request):
		if request.vehicle_type == "car":
			car = CarsModel.get_vehicle(request.vehicle_id)
			if car:
				car_message = CarMessage(car_id = car.car_id, make = car.make,
					model = car.model, year = car.year, 
					co2_grams_per_km = car.co2_grams_per_km,
					created = car.created)
				return VehicleMessage(car = car_message)
			else:
				return VehicleMessage(message = "Vehicle not found")
