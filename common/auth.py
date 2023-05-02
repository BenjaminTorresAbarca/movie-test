from flask import jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from flask import current_app
from flask import request


auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
   if username == "root":
       return "123456"
   return None


@auth.error_handler
def unauthorized():
   current_app.logger.debug(
       "Try an unauthorized access from {} to {} {} with headers {}.".format(
       request.remote_addr,
       request.method,
       request.url,
       request.headers))
   return make_response(jsonify({'error': 'Unauthorized access'}), 403)
