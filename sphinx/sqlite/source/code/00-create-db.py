import sqlite3

db_path = 'app.db'

try:
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()
    sql = '''
    create table user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        password TEXT
    )
    '''

    conn.commit()
finally:
    conn.close()