# coding: utf-8

from flask import Flask, render_template

# Instance
app = Flask(__name__)

# Routing
@app.route("/")
def hello_world():
	names = ["fizz", "buzz", "fuga", "piyo"]
	return render_template("index.html", names=names)

# Appを起動
if __name__ == "__main__":
	app.run()