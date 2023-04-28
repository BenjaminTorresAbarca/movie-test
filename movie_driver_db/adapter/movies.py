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
