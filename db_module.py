import sqlite3

class Database:

    def __init__(self):
        self.conn = None
        self.cursor = None

    def make_connection(self):
        self.conn = sqlite3.connect('')
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.close()

    def execute_query(self, query):
        self.cursor.execute(*query)
        self.conn.commit()

    def select_query(self, query):

        if query == tuple():
            self.cursor.execute(*query)
            result = self.cursor.fetchall()
        else:
            self.cursor.execute(query)
            result = self.cursor.fetchall()

        self.conn.commit()
        return result
