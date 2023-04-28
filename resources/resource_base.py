from flask import jsonify, make_response
from flask_restful import Resource
from common.auth import auth
from flask import current_app
from flask import request


class ResourceBase(Resource):

   def __init__(self):
       current_app.logger.info(
           "Authorized access from {}:{} to {} {}.".format(
           auth.username(),
           request.remote_addr,
           request.method,
           request.url))

   def handle_error(self, exception):
       message = "Unexpected error has ocurred: {}".format(exception)
       current_app.logger.exception(message)
       return make_response(jsonify({'error': message}), 500)
