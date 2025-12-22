# coding: utf-8

"""
かじるプログラミング_sqlite
"""

import sql_lite3

def main():
    """ メイン処理 """
    
    # Sqlite3
    # Create
    sql_lite3.create_table()

    # Insert
    sql_lite3.insert_record("Alex", "Hello, someone there!?")

    # Update
    sql_lite3.update_record(1, "Becky", "Hi, how about you!?")

    # Delete
    #sql_lite3.delete_record(1)

    # Read
    record = sql_lite3.read_record(1)
    print("Record:", record)

if __name__ == "__main__":
    main()