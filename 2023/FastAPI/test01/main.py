# coding: utf-8

"""
Local
1, Install
    $ python3 -m pip install fastapi==0.100.0 'uvicorn[standard]==0.22.0'
2, Run
    $ uvicorn main:app --reload
3, Docs
    http://127.0.0.1:8000/docs
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