import sqlite3
from database import sql_quries

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite3')
        self.cursor = self.conn.cursor()

    def sql_create_tables(self):
        if self.conn:
            print('database connected!')

        self.conn.execute(sql_quries.CREATE_USER_TABLE_QUERY)
        self.conn.commit()

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_quries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name)
        )
        self.conn.commit()

        self.conn.close()