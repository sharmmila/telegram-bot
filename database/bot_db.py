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
        self.conn.execute(sql_quries.CREATE_PROFILE_TABLE_QUERY)
        self.conn.execute(sql_quries.CREATE_LIKE_TABLE_QUERY)
        self.conn.execute(sql_quries.CREATE_DISLIKE_TABLE_QUERY)
        self.conn.execute(sql_quries.CREATE_REFERENCE_TABLE_QUERY)
        self.conn.execute(sql_quries.CREATE_NEWS_TABLE_QUERY)
        self.conn.execute(sql_quries.CREATE_MOVIES_TABLE_QUERY)
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

    def insert_profile(self, tg_id, nickname, bio, age, married, gender, hobbies, location, photo):
        self.cursor.execute(
            sql_quries.INSERT_PROFILE_QUERY,
            (None, tg_id, nickname, bio, age, married, gender, hobbies, location, photo)
        )
        self.conn.commit()

    def select_all_profiles(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "married": row[5],
            "gender": row[6],
            "hobbies": row[7],
            "location": row[8],
            "photo": row[9],
        }
        return self.cursor.execute(
            sql_quries.SELECT_LEFT_JOIN_PROFILE_QUERY,
            (tg_id, tg_id,)
        ).fetchall()

    def insert_like_profile(self, owner, liker):
        self.cursor.execute(
            sql_quries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.conn.commit()

    def select_profile(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "married": row[5],
            "gender": row[6],
            'hobbies': row[7],
            'location': row[8],
            "photo": row[9],
        }
        return self.cursor.execute(
            sql_quries.SELECT_PROFILE_QUERY,
            (tg_id,)
        ).fetchone()

    def update_profile(self, nickname, bio, age, married, gender, hobbies,location, photo, tg_id):
        self.cursor.execute(
            sql_quries.UPDATE_PROFILE_QUERY,
            (nickname, bio, age, married, gender,hobbies, location, photo, tg_id,)
        )
        self.conn.commit()

    def insert_dislike_profile(self, owner, disliker):
        self.cursor.execute(
            sql_quries.INSERT_DISLIKE_QUERY,
            (None, owner, disliker,)
        )
        self.conn.commit()

    def update_user_link(self, link, tg_id):
        self.cursor.execute(
            sql_quries.UPDATE_USER_LINK_QUERY,
            (link, tg_id,)
        )
        self.conn.commit()

    def select_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5],
            "balance": row[6],
        }
        return self.cursor.execute(
            sql_quries.SELECT_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5],
            "balance": row[6],
        }
        return self.cursor.execute(
            sql_quries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()

    def update_owner_balance(self, tg_id):
        self.cursor.execute(
            sql_quries.UPDATE_USER_BALANCE_QUERY,
            (tg_id,)
        )
        self.conn.commit()

    def insert_reference_user(self, owner, reference):
        self.cursor.execute(
            sql_quries.INSERT_REFERENCE_QUERY,
            (None, owner, reference,)
        )
        self.conn.commit()

    def select_reference_user_info(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "balance": row[0],
            "count": row[1]
        }
        return self.cursor.execute(
            sql_quries.SELECT_REFERENCE_USER_INFO_QUERY,
            (tg_id,)
        ).fetchone()

    def select_reference_list(self, tg_id):
        self.cursor.execute(
            sql_quries.SELECT_REFERENCE_LIST,
            (tg_id,)
        )
        self.conn.commit()

    # def insert_news(self, link):
    #     self.cursor.execute(
    #         sql_quries.INSERT_NEWS_QUERY,
    #         (None, link,)
    #     )
    #     self.conn.commit()
    #
    # def insert_movies(self, link):
    #     self.cursor.execute(
    #         sql_quries.INSERT_MOVIES_QUERY,
    #         (None, link,)
    #     )
    #     self.conn.commit()
