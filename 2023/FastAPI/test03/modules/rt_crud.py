# coding: utf-8

from fastapi import APIRouter

# Instance
router = APIRouter()

# Create
@router.get("/menu")
async def create_menu():
	pass

# Read
@router.get("/menu")
async def read_menu():
	pass

# Update
@router.put("/menu/{menu_id}")
async def update_menu():
	pass

# Delete
@router.delete("/menu/{menu_id}")
async def delete_menu():
	pass