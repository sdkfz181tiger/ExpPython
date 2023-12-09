# coding: utf-8

import os
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy
dir_base = os.path.dirname(__file__)
db_path = "sqlite:///" + os.path.join(dir_base, "data.sqlite")
db_table = "records"

# Engine
db_engine = create_engine(db_path, echo=True)
Base = declarative_base()

# CRUD(Create)
def create_table():
	print("create_table:", db_table)
	Base.metadata.create_all(db_engine)

# CRUD(Insert)
def insert_record(name, comment):
	print("insert_record:", name, comment)
	# Session
	session_maker = sessionmaker(bind=db_engine)
	session = session_maker()
	session.add(Record(name, comment))
	session.commit()

# CRUD(Read)
def read_records():
	print("read_records!!")
	# Session
	session_maker = sessionmaker(bind=db_engine)
	session = session_maker()
	return session.query(Record).order_by(Record.uid.desc()).all()

def read_record(uid):
	print("read_record:", uid)
	# Session
	session_maker = sessionmaker(bind=db_engine)
	session = session_maker()
	return session.query(Record).filter(Record.uid==uid).first()

# CRUD(Update)
def update_record(uid, name, comment):
	print("update_record:", uid)
	# Session
	session_maker = sessionmaker(bind=db_engine)
	session = session_maker()
	record = session.query(Record).filter(Record.uid==uid).first()
	record.name = name
	record.comment = comment
	session.commit()
	return read_record(uid)

# CRUD(Delete)
def delete_record(uid):
	print("delete_record:", uid)
	# Session
	session_maker = sessionmaker(bind=db_engine)
	session = session_maker()
	record = session.query(Record).filter(Record.uid==uid).first()
	session.delete(record)
	session.commit()

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

	def __init__(self, name, comment):
		self.name = name
		self.comment = comment

	def __str__(self):
		return "uid:{0}, name:{1}, comment:{2}".format(self.uid, self.name, self.comment)
	