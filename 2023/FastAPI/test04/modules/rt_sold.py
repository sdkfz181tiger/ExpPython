# coding: utf-8

from fastapi import APIRouter

# Instance
router = APIRouter()

# Toggle
@router.put("/menu/sold/{menu_id}")
async def toggle_sold(menu_id: int):
	pass