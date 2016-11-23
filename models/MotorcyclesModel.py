from BaseModel import *

class MotorcyclesModel(BaseModel):

	motorcycle_id = IntegerProperty(required = True)
	make = StringProperty(required = True)
	model = StringProperty(required = True)
	year = IntegerProperty(required = True)
	co2_grams_per_km = FloatProperty(required = True)