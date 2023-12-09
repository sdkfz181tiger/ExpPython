# coding: utf-8

"""
Local
1, Install
	$ python3 -m pip install fastapi==0.100.0 'uvicorn[standard]==0.22.0'
2, Run
	$ uvicorn main:app --reload
3, Docs
	http://127.0.0.1:8000/docs
4, Check
	$ curl -X GET http://127.0.0.1:8000/test
	$ curl -X POST http://127.0.0.1:8000/test
"""

from fastapi import FastAPI
from modules import rt_crud, rt_sold

# Instance
app = FastAPI()
app.include_router(rt_crud.router)
app.include_router(rt_sold.router)

# Routing
@app.get("/")
def hello_world():
	return {"greeting": "Hello, World!!"}