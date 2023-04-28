from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.movie.get_all import GetAllMoviesAPI
from resources.movie.get_one import GetOneMovieAPI
from resources.movie.get_all_active import GetAllMoviesActiveAPI


app = Flask(__name__, static_url_path="")
CORS(app)
app.debug = False

api = Api(app)

api.add_resource(
    GetAllMoviesAPI,
    '/movies',
    endpoint='get_all_movies'
)

api.add_resource(
    GetAllMoviesActiveAPI,
    '/movies_active',
    endpoint='get_all_movies_active'
)


api.add_resource(
    GetOneMovieAPI,
    '/movies/<int:id>',
    endpoint='get_movie'
)



if __name__ == "__main__":
    app.run(debug=False, port=5050)
