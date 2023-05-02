from common.auth import auth
from resources.resource_base import ResourceBase
from flask import jsonify, make_response
from movie_driver_db.adapter.movies import MoviesAdapter


class GetAllMoviesActiveAPI(ResourceBase):
    decorators = [auth.login_required]

    def __init__(self):
        super(GetAllMoviesActiveAPI, self).__init__()

    def get(self):
        try:
            functions = MoviesAdapter()
            rows = functions.list_active()
            return make_response(jsonify(rows), 200)

        except Exception as e:
            return self.handle_error(e)
