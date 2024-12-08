import mysql.connector as sql

import mysql.connector

class Conexao:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'ifnetwork',
        }
        self.conn = None
        self.cursor_dict = None
        self.cursor = None

    def __enter__(self):
        self.conn = mysql.connector.connect(**self.config)
        self.cursor_dict = self.conn.cursor(dictionary=True)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor_dict:
            self.cursor_dict.close()
        if self.conn:
            self.conn.close()
        if self.cursor:
            self.cursor.close()
