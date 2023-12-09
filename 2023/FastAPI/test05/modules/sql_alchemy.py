# coding: utf-8

"""
1, Install
	$ python3 -m pip install sqlalchemy==2.0.15
"""

import datetime, hashlib, os
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound

# SQLAlchemy
dir_base = os.path.dirname(__file__)
db_path = "sqlite:///" + os.path.join(dir_base, "data.sqlite")
db_table = "record"

# Engine
db_engine = create_engine(db_path, echo=True)
db_session = sessionmaker(bind=db_engine)

Base = declarative_base()

# Session
def get_db():
	return db_session()

# Session(For FastAPI)
def get_db_yield():
	db = get_db()
	try:
		yield db
	finally:
		db.close()

# Model
class Record(Base):

	# Table
	__tablename__ = db_table
	# ID
	uid = Column(Integer, primary_key=True, autoincrement=True)
	# Name
	name = Column(String(12), server_default="noname")
	# Comment
	comment = Column(String(24), server_default="nocomment")
	# Timestamp
	time_stamp = Column(String(24), server_default="1970/01/01 00:00:00")

	def __init__(self, name, comment, time_stamp):
		self.name = name
		self.comment = comment
		self.time_stamp = time_stamp

	def __str__(self):
		return "uid:{0}, name:{1}, comment:{2}, time_stamp:{3}".format(
			self.uid, self.name, self.comment, self.time_stamp)

# CRUD(Create)
def create_table():
	print("create_table:", db_table)
	Base.metadata.create_all(db_engine)

def clear_table(db):
	print("clear_table:", db_table)
	db.execute(delete(Record))
	db.commit()

# CRUD(Insert)
def insert_record(db, name, comment):
	print("insert_record:", name, comment)
	record = Record(name, comment, get_time())
	db.add(record)
	db.commit()
	return record.uid

# CRUD(Read)
def read_records(db):
	print("read_records!!")
	stmt = select(Record).order_by(Record.uid.desc())
	return db.scalars(stmt)

def read_record(db, uid):
	print("read_record:", uid)
	try:
		stmt = select(Record).where(Record.uid == uid)
		return db.scalars(stmt).one()
	except NoResultFound:
		return None

# CRUD(Update)
def update_record(db, uid, name, comment):
	print("update_record:", uid)
	record = read_record(db, uid)
	if record == None: return -1
	record.name = name
	record.comment = comment
	record.time_stamp = get_time()
	db.commit()
	return record.uid

# CRUD(Delete)
def delete_record(db, uid):
	print("delete_record:", uid)
	record = read_record(db, uid)
	if record == None: return -1
	db.delete(record)
	db.commit()
	return record.uid

# Hash
def get_hash(text):
	return hashlib.md5(text.encode()).hexdigest()

# Time
def get_time():
	return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
