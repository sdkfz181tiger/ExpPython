# coding: utf-8

import json
from flask import Flask, render_template

# Instance
app = Flask(__name__)

# JSON
with open("./my_data.json") as f:
	json_obj = json.load(f)

# Routing
@app.route("/")
def hello_world():
	return render_template("index.html", data=json_obj["data"])

@app.route("/detail/<int:index>")
def hello_detail(index):
	return render_template("detail.html", data=json_obj["data"], index=index)

# Appを起動
if __name__ == "__main__":
	app.run()