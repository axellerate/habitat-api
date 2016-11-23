from BaseModel import *

class ZeroEmissionsTransportModel(BaseModel):

	vehicle_type = StringProperty(required=True)

	def add_type(self, type):
		pass