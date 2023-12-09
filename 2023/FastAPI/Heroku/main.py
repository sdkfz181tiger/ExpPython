# coding: utf-8

"""
Local
1, Install
	$ python3 -m pip install fastapi==0.100.0 'uvicorn[standard]==0.22.0'
2, Run
	$ uvicorn main:app
3, Docs
	http://127.0.0.1:8000/docs
"""

"""
Heroku:
1, Install HerokuCLI
	$ brew tap heroku/brew && brew install heroku
2, Check
	$ heroku --version
3, Login
	$ heroku login
4, Move to your App directory
	$ cd ~/your-directory
5, Create... "done" is OK!!
	$ heroku create your-fastapi
6, Create files...
	Procfile
		web:uvicorn main:app --reload --host=0.0.0.0 --port=${PORT:-5000}
	requirements.txt
		fastapi
		uvicorn
	runtime.txt
		python-3.11.5
	main.py
		Your code is here...
7, Deploy "done" is OK!!
	$ git init
	$ git add . & git commit -m "first commit"
	$ heroku git:remote -a your-fastapi
	$ git git push heroku master
8, Check and access (You can get new URL!!)
	$ curl https://your-fastapi-xxx.herokuapp.com/
9, Change and deploy
	$ git add . & git commit -m "second commit" & git push heroku master
10, Check remain Eco dyno time...
	$ heroku ps -a your-fastapi
"""

from fastapi import FastAPI

# Instance
app = FastAPI()

# Routing
@app.get("/")
def hello_world():
	return {"greeting": "Hello, World!!"}

@app.get("/morning")
def good_morning():
	return {"greeting": "Good morning!!"}

@app.get("/afternoon")
def good_afternoon():
	return {"greeting": "Good afternoon!!"}

@app.get("/evening")
def good_evening():
	return {"greeting": "Good evening!!"}

@app.get("/night")
def good_night():
	return {"greeting": "Good night!!"}