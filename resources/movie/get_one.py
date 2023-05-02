from common.auth import auth
from flask import jsonify, make_response
from resources.resource_base import ResourceBase
from movie_driver_db.adapter.movies import MoviesAdapter


class GetOneMovieAPI(ResourceBase):
    decorators = [auth.login_required]

    def __init__(self):
        super(GetOneMovieAPI, self).__init__()

    def get(self, id):
        try:
            functions = MoviesAdapter()
            rows = functions.get(id)
            return make_response(jsonify(rows), 200)

        except Exception as e:
            return self.handle_error(e)
