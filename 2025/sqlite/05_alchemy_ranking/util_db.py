# coding: utf-8

"""
1, Install
    $ python3 -m pip install sqlalchemy==2.0.15
"""

import datetime
import os
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    select,
    String
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

class MyDB():

    def __init__(self, path):
        """ コンストラクタ """
        self.dir_base = os.path.dirname(__file__)
        self.db_path = "sqlite:///" + os.path.join(self.dir_base, path)
        # Engine, Session
        self.db_engine = create_engine(self.db_path, echo=True)
        self.db_session = sessionmaker(bind=self.db_engine)
        Base.metadata.create_all(self.db_engine)# テーブルを作る

    # CRUD(Create)
    def insert_record(self, name, comment, score):
        """ データを追加する """
        print("insert_record:", name, comment)
        # Record
        record = Record(
            name=name, 
            comment=comment, 
            score=score, 
            time_stamp=self.get_time())
        with self.db_session() as session:
            session.add(record)
            session.commit()
            return record.uid

    # CRUD(Read)
    def read_records(self, limit=10):
        """ データを読み込む(limit件数まで) """
        print("read_records:", limit)
        with self.db_session() as session:
            stmt = select(Record).order_by(Record.score.desc()).limit(limit)
            return session.scalars(stmt).all()

    def read_record(self, uid):
        """ データを読み込む(1件) """
        print("read_record:", uid)
        with self.db_session() as session:
            return session.get(Record, uid)

    # CRUD(Update)
    def update_record(self, uid, name, comment, score):
        """ データを更新する(1件) """
        print("update_record:", uid)
        with self.db_session() as session:
            record = session.get(Record, uid)
            if record is None: return -1
            record.name = name
            record.comment = comment
            record.score = score
            record.time_stamp = self.get_time()
            session.commit()
            return record.uid

    # CRUD(Delete)
    def delete_record(self, uid):
        """ データを削除する(1件) """
        print("delete_record:", uid)
        with self.db_session() as session:
            record = session.get(Record, uid)
            if record is None: return -1
            session.delete(record)
            session.commit()
            return record.uid

    # Time
    def get_time(self):
        """ 現在日時を取得する """
        return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

# ORM
Base = declarative_base()
class Record(Base):

    # Table
    __tablename__ = "ranking"
    # ID
    uid = Column(Integer, primary_key=True, autoincrement=True)
    # Name
    name = Column(String(12), nullable=False)
    # Comment
    comment = Column(String(24), nullable=False)
    # Score
    score = Column(Integer, nullable=False)
    # Timestamp
    time_stamp = Column(String(24), nullable=False)

    def __str__(self):
        return "uid:{0}, name:{1}, comment:{2}, score:{3}, time_stamp:{4}".format(
            self.uid, self.name, self.comment, self.score, self.time_stamp)