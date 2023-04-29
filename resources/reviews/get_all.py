from common.auth import auth
from resources.resource_base import ResourceBase
from movie_driver_db.adapter.reviews import ReviewsAdapter


class GetAllReviewsAPI(ResourceBase):
    decorators = [auth.login_required]

    def __init__(self):
        super(GetAllReviewsAPI, self).__init__()

    def get(self, movie_id):
        try:
            functions = ReviewsAdapter()
            rows = functions.list(movie_id)
            return rows

        except Exception as e:
            return self.handle_error(e)
