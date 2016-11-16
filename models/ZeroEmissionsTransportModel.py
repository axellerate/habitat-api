from BaseModel import *

class ZeroEmissionsTransportModel(BaseModel):

	type = StringProperty(required = True)

	def add_type(self, type):
		pass