import sqlite3
from pprint import pprint

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

users_data = [
    ('User1', 'example1@gmail.com', '10', '1000'),
    ('User2', 'example2@gmail.com', '20', '1000'),
    ('User3', 'example3@gmail.com', '30', '1000'),
    ('User4', 'example4@gmail.com', '40', '1000'),
    ('User5', 'example5@gmail.com', '50', '1000'),
    ('User6', 'example6@gmail.com', '60', '1000'),
    ('User7', 'example7@gmail.com', '70', '1000'),
    ('User8', 'example8@gmail.com', '80', '1000'),
    ('User9', 'example9@gmail.com', '90', '1000'),
    ('User10', 'example10@gmail.com', '100', '1000')
]

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# cursor.executemany("INSERT INTO Users(username,email,age,balance) VALUES (?,?,?,?)", users_data)
#
# cursor.execute('SELECT id FROM Users')
# user_ids = [row[0] for row in cursor.fetchall()]
# user_ids.sort()
#
# for i in range(0, len(user_ids), 2):
#     user_id = user_ids[i]
#     cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, user_id))
#
# for i in range(0, len(user_ids), 3):
#     user_id = user_ids[i]
#     cursor.execute("DELETE FROM Users WHERE id = ?", (user_id,))
#
# cursor.execute("DELETE FROM Users WHERE id = ? ",(6,))

cursor.execute("SELECT COUNT(*) FROM Users")
total = cursor.fetchone()[0]
print(f'всего пользователей - {total}')
cursor.execute("SELECT SUM(balance) FROM Users")
all_balance = cursor.fetchone()[0]
print(f'всего денег на счетах - {all_balance}')
print(f"{all_balance//total} - средний баланс")
connection.commit()
connection.close()
