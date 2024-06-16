import sqlite3

conn = sqlite3.connect("db.sqlite", check_same_thread=False)

cursor = conn.cursor()