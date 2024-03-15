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
        self.conn.execute(sql_quries.CREATE_BAN_USER_TABLE_QUERY)
        self.conn.commit()

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_quries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name)
        )
        self.conn.commit()

    def select_ban_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'tg_id': row[1],
            'count': row[2]
        }
        return self.cursor.execute(
            sql_quries.SELECT_BAN_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def insert_ban_user(self, tg_id):
        self.cursor.execute(
            sql_quries.INSERT_BAN_USER_QUERY,
            (None, tg_id, None, 1)
        )
        self.conn.commit()

    def update_ban_user(self, tg_id):
        self.cursor.execute(
            sql_quries.UPDATE_BAN_COUNT_QUERY,
            (tg_id,)
        )
        self.conn.commit()
