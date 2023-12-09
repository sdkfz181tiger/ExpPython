# coding: utf-8

from pydantic import BaseModel, Field
from typing import Optional

class MenuModel(BaseModel):
	uid: int
	name: str | None = Field(None, example="モーニングセット")
	comment: str | None = Field(None, example="朝はこれで決まり!!")