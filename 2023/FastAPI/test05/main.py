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
	$ curl -X GET    http://127.0.0.1:8000/menu
	$ curl -X POST   http://127.0.0.1:8000/menu -H "Content-Type: application/json" -d '{"name":"カレーランチ", "comment":"これが究極!!"}'
	$ curl -X PUT    http://127.0.0.1:8000/menu -H "Content-Type: application/json" -d '{"uid":"1", "name":"カレーセット", "comment":"これぞ至高!!"}'
	$ curl -X DELETE http://127.0.0.1:8000/menu/1
"""

from fastapi import FastAPI
from modules import rt_crud, sc_menu

# Instance
app = FastAPI()
app.include_router(rt_crud.router)

# Routing
@app.get("/")
def hello_world():
	return {"greeting": "Hello, World!!"}