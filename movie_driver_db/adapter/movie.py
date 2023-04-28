from movie_driver_db.sqlite.SqliteConnection import SqliteConnection


class MovieAdapter(object):
    def get_all(self):
        connection = SqliteConnection()
        sentence = "SELECT * FROM MOVIES;"
        rows = connection.get_all(sentence)
        print(rows)
        connection.close_connection()
