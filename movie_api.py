from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.movie.get_all import GetAllMoviesAPI
from resources.movie.get_one import GetOneMovieAPI
from resources.movie.delete import DeleteMovieAPI
from resources.movie.get_all_active import GetAllMoviesActiveAPI
from resources.movie.new import NewMovieAPI
from resources.reviews.get_all import GetAllReviewsAPI
from resources.reviews.new import NewReviewAPI



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

api.add_resource(
    DeleteMovieAPI,
    '/movies/<int:id>',
    endpoint='delete_movie'
)

api.add_resource(
    NewMovieAPI,
    '/movies',
    endpoint='new_movie'
)

api.add_resource(
    GetAllReviewsAPI,
    '/reviews/<int:movie_id>',
    endpoint='get_reviews'
)

api.add_resource(
    NewReviewAPI,
    '/reviews',
    endpoint='new_review'
)

if __name__ == "__main__":
    app.run(debug=False, port=5050)
