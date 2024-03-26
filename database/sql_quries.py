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


CREATE_BAN_USER_TABLE_QUERY = '''
CREATE TABLE IF NOT EXISTS ban_users
(
ID INT PRIMARY KEY,
TELEGRAM_ID INT NOT NULL,
USERNAME CHAR(50),
BAN_COUNT INT,
UNIQUE (TELEGRAM_ID)
)
'''

INSERT_BAN_USER_QUERY = '''
 INSERT INTO ban_users VALUES (?, ?, ?)
'''

SELECT_BAN_USER_QUERY = '''
SELECT * FROM ban_users WHERE TELEGRAM_ID = ?

'''

UPDATE_BAN_COUNT_QUERY = '''
UPDATE ban_users SET BAN_COUNT = BAN_COUNT + 1 WHERE TELEGRAM_ID = ?
'''
CREATE_PROFILE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS profile
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
NICKNAME CHAR(50),
BIO TEXT,
AGE INTEGER,
MARRIED CHAR(10),
GENDER CHAR(40),
HOBBIES CHAR(70),
LOCATION CHAR(50),
PHOTO TEXT,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_PROFILE_QUERY = """
INSERT INTO profile VALUES(?,?,?,?,?,?,?,?,?,?)
"""

SELECT_PROFILES_QUERY = """
SELECT * FROM profile
"""

CREATE_LIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS like_profile
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
LIKER_TELEGRAM_ID INTEGER,
UNIQUE(OWNER_TELEGRAM_ID, LIKER_TELEGRAM_ID)
)
"""

INSERT_LIKE_QUERY = """
INSERT INTO like_profile VALUES (?,?,?)
"""

SELECT_LEFT_JOIN_PROFILE_QUERY = """
SELECT * FROM profile
LEFT JOIN like_profile ON profile.TELEGRAM_ID = like_profile.OWNER_TELEGRAM_ID
AND like_profile.LIKER_TELEGRAM_ID = ?
WHERE like_profile.ID IS NULL
AND profile.TELEGRAM_ID != ?
"""

SELECT_PROFILE_QUERY = """
SELECT * FROM profile WHERE TELEGRAM_ID = ?
"""

UPDATE_PROFILE_QUERY = """
UPDATE profile SET NICKNAME = ?, BIO = ?, AGE = ?, MARRIED = ?, GENDER = ?, HOBBIES = ?, 
LOCATION = ?,PHOTO = ? WHERE TELEGRAM_ID = ?
"""

CREATE_DISLIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS dislike_profile
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
DISLIKER_TELEGRAM_ID INTEGER,
UNIQUE(OWNER_TELEGRAM_ID, DISLIKER_TELEGRAM_ID)
)
"""
INSERT_DISLIKE_QUERY = """
INSERT INTO dislike_profile VALUES (?,?,?)
"""

SELECT_LEFT_JOIN_PROFILE_DIS_QUERY = """
SELECT * FROM profile
LEFT JOIN dislike_profile ON profile.TELEGRAM_ID = dislike_profile.OWNER_TELEGRAM_ID
AND dislike_profile.DISLIKER_TELEGRAM_ID = ?
WHERE dislike_profile.ID IS NULL
AND profile.TELEGRAM_ID != ?
"""

ALTER_TABLE_USER_QUERY = """
ALTER TABLE telegram_users ADD COLUMN REFERENCE_LINK TEXT
"""

ALTER_TABLE_USER_V2_QUERY = """
ALTER TABLE telegram_users ADD COLUMN BALANCE INTEGER
"""

UPDATE_USER_LINK_QUERY = """
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID = ?
"""

SELECT_USER_QUERY = """
SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?
"""

SELECT_USER_BY_LINK_QUERY = """
SELECT * FROM telegram_users WHERE REFERENCE_LINK = ?
"""

CREATE_REFERENCE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS reference
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
REFERENCE_TELEGRAM_ID INTEGER,
UNIQUE(OWNER_TELEGRAM_ID, REFERENCE_TELEGRAM_ID)
)
"""

UPDATE_USER_BALANCE_QUERY = """
UPDATE telegram_users SET BALANCE = COALESCE(BALANCE, 0) + 100 WHERE TELEGRAM_ID = ?
"""

INSERT_REFERENCE_QUERY = """
INSERT INTO reference VALUES (?,?,?)
"""

SELECT_REFERENCE_USER_INFO_QUERY = """
SELECT
    COALESCE(telegram_users.BALANCE, 0),
    COUNT(reference.ID)
FROM
    telegram_users
LEFT JOIN
    reference on telegram_users.TELEGRAM_ID = reference.OWNER_TELEGRAM_ID
WHERE
    telegram_users.TELEGRAM_ID = ?
"""

SELECT_REFERENCE_LIST = """
SELECT telegram_users.FIRST_NAME 
FROM reference
INNER JOIN telegram_users ON reference.REFERENCE_TELEGRAM_ID = telegram_users.TELEGRAM_ID
WHERE reference.OWNER_TELEGRAM_ID=? 
"""