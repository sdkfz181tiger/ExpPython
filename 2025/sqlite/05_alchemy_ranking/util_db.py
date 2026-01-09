# coding: utf-8

"""
1, Install
    $ python3 -m pip install sqlalchemy==2.0.15
"""

import datetime, hashlib, os
from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound

class MyDB():

    def __init__(self, path):
        """ コンストラクタ """
        self.dir_base = os.path.dirname(__file__)
        self.db_path = "sqlite:///" + os.path.join(self.dir_base, path)
        # Engine, Database
        self.db_engine = create_engine(self.db_path, echo=True)
        self.db_session = sessionmaker(bind=self.db_engine)
        self.db = self.db_session()

    # CRUD(Create)
    def create_table(self):
        """ テーブルを作る """
        Base.metadata.create_all(self.db_engine)

    # CRUD(Insert)
    def insert_record(self, name, comment, score):
        """ データを追加する """
        print("insert_record:", name, comment)
        record = Record(name, comment, score, self.get_time())
        self.db.add(record)
        self.db.commit()
        return record.uid

    # CRUD(Read)
    def read_records(self, limit=10):
        """ データを読み込む(limit件数まで) """
        print("read_records:", limit)
        stmt = select(Record).order_by(Record.score.desc()).limit(limit)
        return self.db.scalars(stmt).all()

    def read_record(self, uid):
        """ データを読み込む(1件) """
        print("read_record:", uid)
        stmt = select(Record).where(Record.uid == uid)
        return self.db.scalars(stmt).one_or_none()

    # CRUD(Update)
    def update_record(self, uid, name, comment, score):
        """ データを更新する(1件) """
        print("update_record:", uid)
        record = self.read_record(uid)
        if record == None: return -1
        record.name = name
        record.comment = comment
        record.score = score
        record.time_stamp = self.get_time()
        self.db.commit()
        return record.uid

    # CRUD(Delete)
    def delete_record(self, uid):
        """ データを削除する(1件) """
        print("delete_record:", uid)
        record = self.read_record(uid)
        if record == None: return -1
        self.db.delete(record)
        self.db.commit()
        return record.uid

    # Close
    def close(self):
        """ データベースを閉じる """
        self.db.close

    # Time
    def get_time(self):
        """ 現在日時を取得する """
        return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

# Model
Base = declarative_base()
class Record(Base):

    # Table
    __tablename__ = "ranking"
    # ID
    uid = Column(Integer, primary_key=True, autoincrement=True)
    # Name
    name = Column(String(12), server_default="noname")
    # Comment
    comment = Column(String(24), server_default="nocomment")
    # Score
    score = Column(Integer, server_default="0")
    # Timestamp
    time_stamp = Column(String(24), default="1970/01/01 00:00:00")

    def __init__(self, name, comment, score, time_stamp):
        self.name = name
        self.comment = comment
        self.score = score
        self.time_stamp = time_stamp

    def __str__(self):
        return "uid:{0}, name:{1}, comment:{2}, score:{3}, time_stamp:{4}".format(
            self.uid, self.name, self.comment, self.score, self.time_stamp)