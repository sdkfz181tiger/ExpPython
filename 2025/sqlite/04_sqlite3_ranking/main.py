# coding: utf-8

"""
かじるプログラミング_sqlite
"""

import random
import util_db

def main():
    """ メイン処理 """

    # Member
    names = ["Alex", "Becky", "Christy", "David"]
    comments = ["Champion!!", "Nice!!", "Good!!", "OMG...!!"]
    
    # MyDB
    my_db = util_db.MyDB("data.sqlite", "ranking")

    # Create
    my_db.create_table()
    
    # Insert(Random)
    name = random.choice(names)
    comment = random.choice(comments)
    score = random.randint(30, 300)
    my_db.insert_record(name, comment, score)
    
    # Update
    #my_db.update_record(1, "Thomas", "Hi, I'm hacker!!", 777)

    # Delete
    #my_db.delete_record(1)

    # Read(One)
    #record = my_db.read_record(1)
    #print("Record:", record)

    # Read(Ranking)
    records = my_db.read_records(limit=5)
    print("= Ranking =")
    for record in records:
        print("Record:", record)

if __name__ == "__main__":
    main()