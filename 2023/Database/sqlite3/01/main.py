# coding: utf-8

import sql_light3

def main():

	# Create
	sql_light3.create_table()

	# Insert
	sql_light3.insert_record("Alex", "Hello, someone there!?")

	# Update
	#sql_light3.update_record(1, "Becky", "Hi, how about you!?")

	# Delete
	#sql_light3.delete_record(1)

	# Read
	records = sql_light3.read_records()
	for record in records:
		print("Record:", record)

if __name__ == "__main__":
	main()