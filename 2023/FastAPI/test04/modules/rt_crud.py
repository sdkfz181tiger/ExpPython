# coding: utf-8

from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List
import modules.sc_menu as sc

# Instance
router = APIRouter()

#==========
# Request

# Create
class RequestCreate(BaseModel):
	name: str

#==========
# CRUD

# Create
@router.post("/menu" ,response_model=sc.CreateModel)
async def create_menu(req: RequestCreate):
	return sc.CreateModel(uid=1, name=req.name)

# Read
@router.get("/menu", response_model=List[sc.ReadModel])
async def read_menu():
	return [sc.ReadModel(uid=1, name="ランチセット")]

# Update
@router.put("/menu/{menu_id}")
async def update_menu():
	pass

# Delete
@router.delete("/menu/{menu_id}")
async def delete_menu():
	pass