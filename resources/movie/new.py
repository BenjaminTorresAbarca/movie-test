from common.auth import auth
from resources.resource_base import ResourceBase
from movie_driver_db.adapter.movies import MoviesAdapter
from flask import request
import json


class NewMovieAPI(ResourceBase):
    decorators = [auth.login_required]

    def __init__(self):
        super(NewMovieAPI, self).__init__()

    def post(self):
        try:
            functions = MoviesAdapter()
            data = request.data.decode()
            json_data = json.loads(data)
            json_data["method"] = "post"
            return functions.new(json_data)

        except Exception as e:
            return self.handle_error(e)
