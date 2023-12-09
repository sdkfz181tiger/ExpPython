# coding: utf-8

from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest, InternalServerError, NotFound

# Instance
app = Flask(__name__)

# Routing
@app.route("/", methods=["GET", "POST"])
def hello_world():
	name = None
	if request.method == "GET":
		name = request.args.get("name")
	if request.method == "POST":
		name = request.form.get("name")
	return render_template("index.html", name=name)

# Error
@app.errorhandler(BadRequest)
@app.errorhandler(InternalServerError)
@app.errorhandler(NotFound)
def hello_error(error):
	return render_template("error.html", error=error), error.code

# Appを起動
if __name__ == "__main__":
	app.run()