from movie_driver_db.adapter.movies import MoviesAdapter
from movie_driver_db.adapter.reviews import ReviewsAdapter


movie_function = MoviesAdapter()
review_function = ReviewsAdapter()

current_items = 8
current_active_items = 8
item_to_be_delete = 8
current_items_reviews = 5


def test_list():
    assert len(movie_function.list()) == current_items


def test_one():
    assert len(movie_function.get(1)) == 1


def test_list_active():
    assert len(movie_function.list_active()) == current_active_items


def test_new_movie():
    dict_movie = {
        "name": "Testing name 3",
        "type": "Action",
        "year": "2015",
        "duration": "2hr 15m",
        "rating": 4.4,
        "director": "Sam Smith"
    }
    assert movie_function.new(dict_movie) == "Movie was created"


def test_delete_movie():
    assert movie_function.delete(item_to_be_delete) == "Movie was deleted"


def test_list_reviews():
    assert len(review_function.list(1)) == current_items_reviews


def test_new_review():
    dict_review = {
        "rate": 5,
        "opinion": "It great",
        "movie_id": 1,
        "comment_by": "juanlo",
    }
    assert review_function.new(dict_review) == "Review was created"
