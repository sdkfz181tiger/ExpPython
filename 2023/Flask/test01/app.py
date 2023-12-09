# coding: utf-8

"""
	1, Install
		python3 -m pip install flask==2.3.2
	2, Run
		python3 app.py
	3, Access on your browser!!
		http://127.0.0.1:5000
"""

from flask import Flask

# Instance
app = Flask(__name__)

# Routing
@app.route("/")
def hello_world():
	return "<h1>Hello, Flask!!</h1>"

@app.route("/welcome")
def hello_welcome():
	return "<h1>This is Welcome page!!</h1>"

@app.route("/about")
def hello_about():
	return "<h1>This is about page!!</h1>"

@app.route("/dynamic1/<prm>")
def hello_dynamic1(prm):
	print(f"type:{type(prm)}, param:{prm}")
	return f"<h1>Parameter is {prm}!!</h1>"

@app.route("/dynamic2/<int:prm>")
def hello_dynamic2(prm):
	print(f"type:{type(prm)}, param:{prm}")
	return f"<h1>Parameter is {prm}!!</h1>"

@app.route("/dynamic3/<float:prm>")
def hello_dynamic3(prm):
	print(f"type:{type(prm)}, param:{prm}")
	return f"<h1>Parameter is {prm}!!</h1>"

@app.route("/dynamic4/<prm1>/<prm2>")
def hello_dynamic4(prm1, prm2):
	print(f"type:{type(prm1)}, param:{prm1}")
	print(f"type:{type(prm2)}, param:{prm2}")
	return f"<h1>Parameters are {prm1} and {prm2}!!</h1>"

# Appを起動
if __name__ == "__main__":
	app.run()