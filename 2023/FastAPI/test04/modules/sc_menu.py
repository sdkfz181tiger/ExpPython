# coding: utf-8

from pydantic import BaseModel, Field
from typing import Optional

class MenuModel(BaseModel):
	uid: int
	name: Optional[str] = Field(None, example="モーニングセット")
	sold: bool = Field(False, description="売り切れ")

class CreateModel(MenuModel):
	pass

class ReadModel(MenuModel):
	pass