# coding: utf-8

from flask import Flask, render_template

# Instance
app = Flask(__name__)

# Routing
@app.route("/")
def hello_world():
	return render_template("index.html")

@app.route("/detail/<int:id>")
def hello_detail(id):
	return render_template("detail.html", id=id)

# Appを起動
if __name__ == "__main__":
	app.run()