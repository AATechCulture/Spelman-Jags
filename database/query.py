import sqlite3
cx = sqlite3.connect("profile_information.db")
cu = cx.cursor()

cu.execute('SELECT * FROM Users')