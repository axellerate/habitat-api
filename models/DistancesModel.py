from BaseModel import *

class Distances(BaseModel):

	"""
	Contains emissions data from each user.
	Emissions can be calcluated on the fly 
	from this table
	"""

	user = ndb.KeyProperty(kind = "Users")
	distance = ndb.IntegerProperty(default = 0)