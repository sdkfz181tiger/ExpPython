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

from fastapi import FastAPI, Header, Path, Query

# Instance
app = FastAPI()

# Routing
@app.get("/")
def hello_world():
    return {"greeting": "Hello, World!!"}

# GET
@app.get("/menu1")
def get_menu()->list[dict[str, str]]:
    return [{"name": "curry"}]

# POST
@app.post("/menu1")
def post_menu()->dict[str, str]:
    return {"name": "rice"}

# GET
@app.get("/menu2")
def get_menu()->list[dict[str, str|int]]:
    return [{"name": "udon", "price": 350}]

# GET
@app.get("/menu3/{order}")
def get_menu(order:int)->list[dict[str, str|int]]:
    return [{"name": "udon", "price": 350, "order": order}]

# GET
@app.get("/menu4")
def get_menu()->list[dict[str, str|int]]:
    return [{"name": "udon", "price": 350}]

# GET http://127.0.0.1:8000/menu5/88
@app.get("/menu5/{order}")
def get_menu(order:int=Path())->list[dict[str, str|int]]:
    return [{"name": "udon", "price": 350, "order": order}]

# GET http://127.0.0.1:8000/menu5?order=88
@app.get("/menu6")
def get_menu(order:int=Query(0))->list[dict[str, str|int]]:
    return [{"name": "udon", "price": 350, "order": order}]