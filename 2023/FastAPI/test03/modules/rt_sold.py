# coding: utf-8

from fastapi import APIRouter

# Instance
router = APIRouter()

# Mark
@router.put("/menu/{menu_id}/done")
async def mark_menu_as_done():
	pass

# Unmark
@router.delete("/menu/{menu_id}/done")
async def unmark_menu_as_done():
	pass