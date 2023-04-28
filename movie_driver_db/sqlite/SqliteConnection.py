import sqlite3
import configparser


class Db2Connection(object):

    def __init__(self):
        self._create_conn()

    def _create_conn(self):
        config = configparser.ConfigParser()
        config.read('../../config.ini')
        self.conn = sqlite3.connect(config['database']['database'])
        self.cursor = self.conn.cursor()

    def execute(self, sentence):
        self.cursor.execute(sentence)

    def get_one(self, sentence):
        self.cursor.execute(sentence)
        return self.cursor.fetchone()

    def get_all(self, sentence):
        self.cursor.execute(sentence)
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
