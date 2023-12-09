# coding: utf-8

"""
1, Install
	$ python3 -m pip install wtforms==3.0.1
	$ python3 -m pip install email-validator==2.0.0.post2
	$ python3 -m pip install sqlalchemy==2.0.15
"""

import db
from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest, InternalServerError, NotFound
from forms import InsertForm, EditForm, DeleteForm

# Instance
app = Flask(__name__)

# Routing
@app.route("/", methods=["GET", "POST"])
def hello_world():
	# Form
	ins_form = InsertForm(request.form)
	del_form = DeleteForm(request.form)
	# POST
	if request.method == "POST":
		# Insert
		if request.form["submit"] == "New":
			if ins_form.validate():# Validate
				db.insert_record(ins_form.name.data, ins_form.comment.data)
		# Delete
		if request.form["submit"] == "Del":
			if del_form.validate():# Validate
				db.delete_record(del_form.uid.data)

	records = db.read_records()# Read
	return render_template("index.html", ins_form=ins_form, del_form=del_form, records=records)

@app.route("/edit/<int:uid>", methods=["GET", "POST"])
def hello_edit(uid):
	# Form
	edit_form = EditForm(request.form)
	record = db.read_record(uid)# Read
	# POST
	if request.method == "POST":
		# Edit
		if request.form["submit"] == "Edit":
			if edit_form.validate():# Validate
				record = db.update_record(uid, edit_form.name.data, edit_form.comment.data)

	return render_template("edit.html", edit_form=edit_form, uid=uid, record=record)

# Error
@app.errorhandler(BadRequest)
@app.errorhandler(InternalServerError)
@app.errorhandler(NotFound)
def hello_error(error):
	return render_template("error.html", error=error), error.code

# Appを起動
if __name__ == "__main__":
	db.create_table()
	app.run()