from movie_driver_db.sqlite.SqliteConnection import SqliteConnection


class ReviewsAdapter(object):
    def list(self, movie_id):
        connection = SqliteConnection()
        sentence = "SELECT * FROM reviews WHERE movie_id = '" + str(movie_id) + "';"
        rows = connection.get_all(sentence)
        list_to_return = []
        for row in rows:
            dict_to_return = {
                "id": row[0],
                "rate": row[1],
                "opinion": row[2],
                "movie_id": row[3],
                "user_id": row[4]
            }
            list_to_return.append(dict_to_return)
        connection.close_connection()
        return list_to_return

    def new(self, review_data):
        if review_data["rate"] is None or review_data["opinion"] is None or review_data[
                "movie_id"] is None or review_data["comment_by"] is None :
            return "Information missing"
        connection = SqliteConnection()

        sentence_insert = "INSERT INTO REVIEWS (rate, opinion, movie_id, comment_by) VALUES ('" + str(
            review_data["rate"]) + "','" + str(review_data["opinion"]) + "','" + str(
            review_data["movie_id"]) + "','" + str(review_data["comment_by"]) + "')"
        connection.execute(sentence_insert)
        connection.commit()
        connection.close_connection()
        return "Movie was created"
