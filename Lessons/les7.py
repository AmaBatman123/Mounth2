# SQL
import sqlite3 as sq

with sq.connect('test.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio VARCHAR(20),
    old INT DEFAULT 0    
    )''')
    # cursor.execute('''INSERT INTO users(fio, old)
    # VALUES
    # ('Muda Bek', 62),
    # ('Gena', 33)''')

    cursor.execute('''SELECT fio,old FROM users''')
    # print(cursor.fetchall()) Вывод всего, что есть в селекте
    for row in cursor:
        print(row)

    cursor.execute('''UPDATE users SET fio='Master BEKA' WHERE id=1''')

    cursor.execute('''SELECT * FROM users''')
    for row in cursor:
        print(row)

    cursor.execute('''DELETE FROM users WHERE id=3''')
    cursor.execute('''SELECT * FROM users''')
    for row in cursor:
        print(row)