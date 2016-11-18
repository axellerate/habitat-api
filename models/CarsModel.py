from BaseModel import *
from messages.cars_messages import *
from xml.dom import minidom
import urllib

# this two functions parse FuelEconomy.gov xml
# for car data

def get_XML_document_for_car_id(car_id):
	url_string = "http://www.fueleconomy.gov/ws/rest/vehicle/" + str(car_id)
	xml_string = urllib.urlopen(url_string).read()
	xml_document = minidom.parseString(xml_string)
	return xml_document

def get_value_from_xml(xml_document, tag_name):
	node = xml_document.getElementsByTagName(tag_name)
	value = node[0].firstChild.nodeValue
	return value

class CarsModel(BaseModel):

	"""
	Stores the car data from http://www.FuelEconomy.gov
	"""

	car_id = ndb.IntegerProperty(required = True)
	make = ndb.StringProperty(required = True)
	model = ndb.StringProperty(required = True)
	year = ndb.IntegerProperty(required = True)
	co2_grams_per_km = ndb.FloatProperty(required = True)

	def to_message(self):
		return CarMessage(car_id = self.car_id,
							make = self.make,
							model = self.model,
							year = self.year,
							co2_grams_per_km = self.co2_grams_per_km)

	@classmethod
	def get_vehicles(cls):
		return cls.query()

	@classmethod
	def get_vehicle(cls, car_id):
		car = cls.query(cls.car_id == int(car_id)).get()
		return car

	@classmethod
	def add_vehicle(cls, car_id):
		car_exists = cls.query(cls.car_id == int(car_id)).get()
		if not car_exists:

			xml_document = get_XML_document_for_car_id(car_id)

			new_car = cls()
			new_car.car_id = int(car_id)
			new_car.make = get_value_from_xml(xml_document, "make")
			new_car.model = get_value_from_xml(xml_document, "model")
			new_car.year = int(get_value_from_xml(xml_document, "year"))
			new_car.co2_grams_per_km = float(get_value_from_xml(xml_document, "co2TailpipeGpm")) / 1.67
			new_car.put()
			return new_car
		else:
			return cls()
