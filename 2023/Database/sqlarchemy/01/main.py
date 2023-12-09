# coding: utf-8

import sql_alchemy

def main():

	# Create
	sql_alchemy.create_table()

	# Session
	db = sql_alchemy.get_db()

	# Clear
	#sql_alchemy.clear_table(db)

	# Insert
	uid = sql_alchemy.insert_record(db, "Hello", "SQLAlchemy!!")
	print("Insert:", uid)

	# Update
	uid = sql_alchemy.update_record(db, 1, "Byebye", "SQLite3!!")
	print("Update:", uid)

	# Delete
	#uid = sql_alchemy.delete_record(db, 1)
	#print("Delete:", uid)

	# Read
	#record = sql_alchemy.read_record(db, 1)
	#print("Record(One):", record)

	# Read
	records = sql_alchemy.read_records(db)
	for record in records:
		print("Record(All):", record)

	# Close
	db.close()

if __name__ == "__main__":
	main()