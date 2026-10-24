# coding: utf-8

"""
1, Install
    $ python3 -m pip install pysqlite3
"""

import datetime
import os
import sqlite3

class MyDB():

    def __init__(self, path, table):
        """ コンストラクタ """
        self.dir_base = os.path.dirname(__file__)
        self.db_path = os.path.join(self.dir_base, path)
        self.db_table = table

    # CRUD(Create)
    def create_table(self):
        """ テーブルを作る """
        # SQLite
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS {0}(
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT DEFAULT "noname",
            comment TEXT DEFAULT "nocomment",
            score INTEGER DEFAULT 0,
            time_stamp TEXT DEFAULT "1970/01/01 00:00:00")
            """.format(self.db_table)
        cur.execute(sql)
        con.commit()# Important
        con.close()

    # CRUD(Insert)
    def insert_record(self, name, comment, score):
        """ データを追加する """
        # SQLite
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = """
            INSERT INTO {0} VALUES(?, ?, ?, ?, ?)
            """.format(self.db_table)
        cur.execute(sql, (None, name, comment, score, self.get_time()))
        con.commit()# Important
        con.close()

    # CRUD(Read)
    def read_records(self, limit=10):
        """ データを読み込む(limit件数まで) """
        # SQLite
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = """
            SELECT * FROM {0} ORDER BY score DESC LIMIT ?
            """.format(self.db_table)
        cur.execute(sql, (limit,))
        records = cur.fetchall()
        con.close()
        return records

    def read_record(self, uid):
        """ データを読み込む(1件) """
        # SQLite
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = """
            SELECT * FROM {0} WHERE uid=?
            """.format(self.db_table)
        cur.execute(sql, (uid,))
        record = cur.fetchone()
        con.close()
        return record

    # CRUD(Update)
    def update_record(self, uid, name, comment, score):
        """ データを更新する(1件) """
        # SQLite
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = """
            UPDATE {0} SET name=?, comment=?, score=?, time_stamp=? WHERE uid=?
            """.format(self.db_table)
        cur.execute(sql, (name, comment, score, self.get_time(), uid))
        con.commit()# Important
        con.close()
        return self.read_record(uid)

    # CRUD(Delete)
    def delete_record(self, uid):
        """ データを削除する(1件) """
        # SQLite
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = """
            DELETE FROM {0} WHERE uid=?
            """.format(self.db_table)
        cur.execute(sql, (uid,))
        con.commit()# Important
        con.close()

    # Time
    def get_time(self):
        """ 現在日時を取得する """
        return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
