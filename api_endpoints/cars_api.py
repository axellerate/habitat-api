from google.appengine.ext import endpoints

from xml.dom import minidom
import urllib

from protorpc import message_types
from protorpc import remote

from models.CarsModel import *

def getXMLDocumentForCarId(car_id):
	url_string = "http://www.fueleconomy.gov/ws/rest/vehicle/" + car_id
	xml_string = urllib.urlopen(url_string).read()
	xml_document = minidom.parseString(xml_string)
	return xml_document

def getValueFromXML(xml_document, tag_name):
	node = xml_document.getElementsByTagName(tag_name)
	value = node[0].firstChild.nodeValue
	return value

@endpoints.api(name='cars', version='v1',
				description='Cars API')
class CarsAPI(remote.Service):
	"""Class which defines Cars API v1."""

	@endpoints.method(message_types.VoidMessage, CarsMessage,
						path='cars/all', http_method='GET',
						name='all')
	def getAllCars(self, request):
		cars = Cars.query()
		items = [car.to_message() for car in cars]
		return CarsMessage(cars = items)

	@endpoints.method(CarAddMessage, CarMessage,
						path='cars/get_by_id', http_method='GET',
						name='get_by_id')
	def getCarById(self, request):
		car = Cars.query(Cars.car_id == int(request.car_id)).get()
		if car:
			car_message = CarMessage(car_id = car.car_id,
									 make = car.make,
									 model = car.model,
									 year = car.year,
									 emissions_per_mile = car.emissions_per_mile)
			return car_message


	@endpoints.method(CarAddMessage, CarMessage,
						path='cars', http_method='POST',
						name='add')
	def addCar(self, request):

		car_exists = Cars.query(Cars.car_id == int(request.car_id)).get()

		if not car_exists:

			xml_document = getXMLDocumentForCarId(request.car_id)

			car_message = CarMessage()

			car_message.car_id = int(request.car_id)
			car_message.make = getValueFromXML(xml_document, "make")
			car_message.model = getValueFromXML(xml_document, "model")
			car_message.year = int(getValueFromXML(xml_document, "year"))
			car_message.emissions_per_mile = float(getValueFromXML(xml_document, 
																"co2TailpipeGpm"))
			Cars.addNewCar(car_message)

			return car_message