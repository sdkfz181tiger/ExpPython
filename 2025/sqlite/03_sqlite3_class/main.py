# coding: utf-8

"""
かじるプログラミング_sqlite
"""

import util_db

def main():
    """ メイン処理 """
    
    # MyDB
    my_db = util_db.MyDB("data.sqlite", "records")

    # Create
    my_db.create_table()
    
    # Insert
    my_db.insert_record("Alex", "Hello, someone there!?")
    
    # Update
    my_db.update_record(1, "Becky", "Hi, how about you!?")

    # Delete
    #my_db.delete_record(1)

    # Read
    record = my_db.read_record(1)
    print("Record:", record)

if __name__ == "__main__":
    main()