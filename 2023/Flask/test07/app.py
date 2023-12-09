# coding: utf-8

from flask import Flask, render_template
from werkzeug.exceptions import BadRequest, InternalServerError, NotFound

# Instance
app = Flask(__name__)

# Routing
@app.route("/")
def hello_world():
	return render_template("index.html")

# Error
@app.errorhandler(BadRequest)
@app.errorhandler(InternalServerError)
@app.errorhandler(NotFound)
def hello_error(error):
	return render_template("error.html", error=error), error.code

# Appを起動
if __name__ == "__main__":
	app.run()