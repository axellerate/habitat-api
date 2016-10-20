from BaseModel import *

class Emissions(BaseModel):

	"""
	Stores the emissions data
	"""

	distance = ndb.KeyProperty(kind = "Distances")
	transport = ndb.KeyProperty(kind = "Transportation")
	emissions = ndb.FloatProperty(default = 0)