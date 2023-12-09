# coding: utf-8

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import List
import modules.sc_menu as sc
import modules.sql_alchemy as ar

# Instance
router = APIRouter()

# SQLAlchemy
ar.create_table()

#==========
# Convert (Records -> Model)
def convertRecord2Model(record):
	if(record==None): return sc.MenuModel(uid=-1, name="", comment="")
	return sc.MenuModel(uid=record.uid, name=record.name, comment=record.comment)

#==========
# Request

# Create
class RequestCreate(BaseModel):
	name: str
	comment: str

class RequestUpdate(BaseModel):
	uid: int
	name: str
	comment: str

#==========
# CRUD

# Create
@router.post("/menu")
async def create_menu(db:Session=Depends(ar.get_db_yield), req:RequestCreate=None):
	uid = ar.insert_record(db, **req.dict())
	return {"uid": uid}

# Read
@router.get("/menu", response_model=List[sc.MenuModel])
async def read_menu_all(db:Session=Depends(ar.get_db_yield)):
	records = ar.read_records(db)
	list = []
	for record in records:
		list.append(convertRecord2Model(record))
	return list

# Read
@router.get("/menu/{uid}", response_model=sc.MenuModel)
async def read_menu_one(db:Session=Depends(ar.get_db_yield), uid:int=-1):
	record = ar.read_record(db, uid)
	return convertRecord2Model(record)

# Update
@router.put("/menu")
async def update_menu(db:Session=Depends(ar.get_db_yield), req:RequestUpdate=None):
	uid = ar.update_record(db, **req.dict())
	return {"uid": uid}

# Delete
@router.delete("/menu/{uid}")
async def delete_menu(db:Session=Depends(ar.get_db_yield), uid:int=-1):
	uid = ar.delete_record(db, uid=uid)
	return {"uid": uid}
