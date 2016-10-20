from google.appengine.ext import endpoints

from xml.dom import minidom
import urllib

from protorpc import message_types
from protorpc import remote

from models import *

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
						path='cars', http_method='GET',
						name='all')
	def getAllCars(self, request):
		cars = Cars.query()
		items = [car.to_message() for car in cars]
		return CarsMessage(cars = items)

	@endpoints.method(CarAddMessage, CarMessage,
						path='cars', http_method='POST',
						name='add')
	def addCar(self, request):

		car_exists = Cars.query(Cars.car_id == int(request.car_id)).get()

		if not car_exists:

			xml_document = getXMLDocumentForCarId(request.car_id)

			carMessage = CarMessage()

			carMessage.car_id = int(request.car_id)
			carMessage.make = getValueFromXML(xml_document, "make")
			carMessage.model = getValueFromXML(xml_document, "model")
			carMessage.year = int(getValueFromXML(xml_document, "year"))
			carMessage.emissions_per_mile = float(getValueFromXML(xml_document, 
																"co2TailpipeGpm"))
			Cars.addNewCar(carMessage)

			return carMessage