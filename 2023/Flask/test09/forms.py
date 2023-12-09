# coding: utf-8

from wtforms import (
	Form, PasswordField, StringField, SubmitField, 
	validators)

class UserInfoForm(Form):
	# Name
	name = StringField("Name", validators=[
		validators.DataRequired(message="Nameを入力してください")])
	# Email
	email = StringField("Email Address", validators=[
		validators.DataRequired(message="Emailを入力してください"),
		validators.Email("Emailを正しく入力してください")])
	# Password(input)
	password = PasswordField("New Password", validators=[
		validators.DataRequired(message="パスワードを入力してください")
	])
	# Password(confirm)
	confirm = PasswordField("Repeat Password", validators=[
		validators.EqualTo("password", message="パスワードが一致しません")])
	# Submit
	submit = SubmitField("Submit")