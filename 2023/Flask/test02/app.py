# coding: utf-8

from flask import Flask, render_template

# Instance
app = Flask(__name__)

# Routing
@app.route("/")
def hello_world():
	return render_template("index.html")

@app.route("/welcome")
def hello_welcome():
	return render_template("welcome.html")

@app.route("/greeting")
def hello_greeting():
	return render_template("greeting.html")

# Appを起動
if __name__ == "__main__":
	app.run()