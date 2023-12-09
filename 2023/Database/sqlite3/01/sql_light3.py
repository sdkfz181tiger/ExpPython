# coding: utf-8

"""
1, Install
	$ python3 -m pip install pysqlite3
"""

import datetime, hashlib, os, sqlite3

# SQLite
dir_base = os.path.dirname(__file__)
db_path = os.path.join(dir_base, "data.sqlite")
db_table = "records"

# CRUD(Create)
def create_table():
	print("create_table:", db_table)
	# SQLite
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	sql = """CREATE TABLE IF NOT EXISTS {0}(
		uid INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT DEFAULT "noname",
		comment TEXT DEFAULT "nocomment",
		time_stamp TEXT DEFAULT "1970/01/01 00:00:00")
		""".format(db_table)
	cur.execute(sql)
	con.commit()# Important
	con.close()

# CRUD(Insert)
def insert_record(name, comment):
	print("insert_record:", name, comment)
	# SQLite
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	sql = "INSERT INTO {0} VALUES(?, ?, ?, ?)".format(db_table)
	print(sql)
	cur.execute(sql, (None, name, comment, get_time()))
	con.commit()# Important
	con.close()

# CRUD(Read)
def read_records():
	print("read_records!!")
	# SQLite
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	sql = "SELECT * FROM {0} ORDER BY uid DESC".format(db_table)
	cur.execute(sql)
	records = cur.fetchall()
	con.close()
	return records

def read_record(uid):
	print("read_record:", uid)
	# SQLite
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	sql = "SELECT * FROM {0} WHERE uid=?".format(db_table)
	cur.execute(sql, (uid,))
	record = cur.fetchone()
	con.close()
	return record

# CRUD(Update)
def update_record(uid, name, comment):
	print("update_record:", uid)
	# SQLite
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	sql = "UPDATE {0} SET name=?, comment=?, time_stamp=? WHERE uid=?".format(db_table)
	cur.execute(sql, (name, comment, get_time(), uid))
	con.commit()# Important
	con.close()
	return read_record(uid)

# CRUD(Delete)
def delete_record(uid):
	print("delete_record:", uid)
	# SQLite
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	sql = "DELETE FROM {0} WHERE uid=?".format(db_table)
	cur.execute(sql, (uid,))
	con.commit()# Important
	con.close()

# Hash
def get_hash(text):
	return hashlib.md5(text.encode()).hexdigest()

# Time
def get_time():
	return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")