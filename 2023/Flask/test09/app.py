# coding: utf-8

"""
1, Install
	$ python3 -m pip install wtforms==3.0.1
	$ python3 -m pip install email-validator==2.0.0.post2
"""

from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest, InternalServerError, NotFound
from forms import UserInfoForm

# Instance
app = Flask(__name__)

# Routing
@app.route("/", methods=["GET", "POST"])
def hello_world():
	# Form
	form = UserInfoForm(request.form)
	# POST and Validation OK!!
	if request.method == "POST" and form.validate():
		return render_template("result.html", form=form)
	return render_template("index.html", form=form)

# Error
@app.errorhandler(BadRequest)
@app.errorhandler(InternalServerError)
@app.errorhandler(NotFound)
def hello_error(error):
	return render_template("error.html", error=error), error.code

# Appを起動
if __name__ == "__main__":
	app.run()