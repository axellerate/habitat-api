from protorpc import messages
from cars_messages import *

class UserMessage(messages.Message):
	email = messages.StringField(1)
	nickname = messages.StringField(2)
	user_id = messages.StringField(3)