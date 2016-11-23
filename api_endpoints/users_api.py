import endpoints
import json
import os
from google.appengine.api import urlfetch

from protorpc import message_types
from protorpc import remote

from models.UsersModel import UsersModel
from messages.users_messages import *

def get_user_id():
    """A workaround implementation for getting userid."""
    auth = os.getenv('HTTP_AUTHORIZATION')
    bearer, token = auth.split()
    token_type = 'id_token'
    if 'OAUTH_USER_ID' in os.environ:
        token_type = 'access_token'
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?%s=%s'
           % (token_type, token))
    user = {}
    wait = 1
    for i in range(3):
        resp = urlfetch.fetch(url)
        if resp.status_code == 200:
            user = json.loads(resp.content)
            break
        elif resp.status_code == 400 and 'invalid_token' in resp.content:
            url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?%s=%s'
                   % ('access_token', token))
        else:
            time.sleep(wait)
            wait = wait + i
    return user.get('user_id', '')

@endpoints.api(name='users', version='v1',
				description='Users API')
class UsersAPI(remote.Service):
	"""Class which defines Users API v1."""

	@endpoints.method(message_types.VoidMessage, UserMessage,
						path='users', http_method='POST',
						name='add')
	def add_user(self, request):
		current_user = endpoints.get_current_user()
		if current_user is None:
			raise endpoints.UnauthorizedException('Invalid token.')
		else:
			current_user_id = get_user_id()
			user = UsersModel.add_user(current_user_id).get()
			return UserMessage(email = current_user.email(), user_id = user.google_user_id)

	@endpoints.method(message_types.VoidMessage, UserMessage,
						path='users', http_method='GET',
						name='get')
	def get_user(self, request):
		current_user = endpoints.get_current_user()
		if current_user is None:
			raise endpoints.UnauthorizedException('Invalid token.')
		else:
			current_user_id = get_user_id()
			user = UsersModel.query(UsersModel.google_user_id == current_user_id).get()
			return UserMessage(email = current_user.email(), user_id = user.google_user_id)