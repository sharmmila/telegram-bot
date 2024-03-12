CREATE_USER_TABLE_QUERY = '''
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INT PRIMARY KEY,
TELEGRAM_ID INT NOT NULL,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
'''

INSERT_USER_QUERY = '''
 INSERT INTO telegram_users VALUES (?, ?, ?, ?, ?)
'''