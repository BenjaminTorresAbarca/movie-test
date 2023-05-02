from movie_driver_db.sqlite.SqliteConnection import SqliteConnection


class MoviesAdapter(object):
    def list(self):
        connection = SqliteConnection()
        sentence = "SELECT * FROM MOVIES;"
        rows = connection.get_all(sentence)
        list_to_return = []
        for row in rows:
            dict_to_return = {
                "id": row[0],
                "name": row[1],
                "type": row[2],
                "year": row[3],
                "duration": row[4],
                "rating": row[5],
                "director": row[6],
                "status": row[7]
            }
            list_to_return.append(dict_to_return)
        connection.close_connection()
        return list_to_return

    def list_active(self):
        connection = SqliteConnection()
        sentence = "SELECT * FROM MOVIES WHERE STATUS = 'Active';"
        rows = connection.get_all(sentence)
        list_to_return = []
        for row in rows:
            dict_to_return = {
                "id": row[0],
                "name": row[1],
                "type": row[2],
                "year": row[3],
                "duration": row[4],
                "rating": row[5],
                "director": row[6],
                "status": row[7]
            }
            list_to_return.append(dict_to_return)
        connection.close_connection()
        return list_to_return

    def get(self, id):
        connection = SqliteConnection()
        sentence = "SELECT * FROM MOVIES WHERE ID = '" + str(id) + "';"
        row = connection.get_one(sentence)
        list_to_return = []
        if row:
            dict_to_return = {
                "id": row[0],
                "name": row[1],
                "type": row[2],
                "year": row[3],
                "duration": row[4],
                "rating": row[5],
                "director": row[6],
                "status": row[7]
            }
            list_to_return.append(dict_to_return)
        connection.close_connection()
        return list_to_return

    def new(self, movie_data):
        if movie_data["name"] is None or movie_data["type"] is None or movie_data["year"] is None or movie_data[
                "duration"] is None or movie_data["rating"] is None or movie_data["director"] is None:
            return "Information missing"
        connection = SqliteConnection()
        sentence_exist = "SELECT * FROM MOVIES WHERE NAME = '" + str(movie_data["name"]) + "';"
        exist = connection.get_all(sentence_exist)
        if exist:
            connection.close_connection()
            return "This movie was already created"
        else:
            sentence_insert = "INSERT INTO MOVIES (name, type, year, duration, rating, director, status) VALUES ('" + str(
                movie_data["name"]) + "','" + str(movie_data["type"]) + "','" + str(movie_data["year"]) + "','" + str(
                movie_data["duration"]) + "','" + str(movie_data["rating"]) + "','" + str(
                movie_data["director"]) + "','Active')"
            connection.execute(sentence_insert)
            connection.commit()
            connection.close_connection()
            return "Movie was created"

    def update_rating(self, rating_dict):
        connection = SqliteConnection()
        sentence = "UPDATE MOVIES SET rating = '" + str(rating_dict["rating"]) + "' WHERE ID = '" + str(
            rating_dict["movie_id"]) + "'"
        connection.execute(sentence)
        connection.commit()
        connection.close_connection()

    def delete(self, id):
        connection = SqliteConnection()
        sentence = "SELECT * FROM MOVIES WHERE ID = '" + str(id) + "';"
        row = connection.get_one(sentence)
        if row:
            sentence = "DELETE FROM MOVIES WHERE ID = '" + str(id) + "';"
            connection.execute(sentence)
            return "Movie was deleted"
        else:
            connection.close_connection()
            return "This movie does not exist"
