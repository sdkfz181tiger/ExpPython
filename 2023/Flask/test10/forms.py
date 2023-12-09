# coding: utf-8

from wtforms import (
	Form, StringField, SubmitField, 
	validators)

class InsertForm(Form):
	# Name
	name = StringField("Name", validators=[
		validators.DataRequired(message="Nameを入力してください")])
	# Comment
	comment = StringField("Comment", validators=[
		validators.DataRequired(message="Commentを入力してください")])
	# Submit
	submit = SubmitField("New")

class EditForm(Form):
	# Name
	name = StringField("Name", validators=[
		validators.DataRequired(message="Nameを入力してください")])
	# Comment
	comment = StringField("Comment", validators=[
		validators.DataRequired(message="Commentを入力してください")])
	# Submit
	submit = SubmitField("Edit")

class DeleteForm(Form):
	# UID
	uid = StringField("UID")
	# Submit
	submit = SubmitField("Del")
