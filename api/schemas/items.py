from typing import List, Union
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    description: str
    tags: Union[List[str], None] = None

    class Config:
        orm_mode = True


class ItemReturn(BaseModel):
    id: int
    description: str


class ItemCreate(BaseModel):
    description: str
    tags: List[str]


class ItemUpdate(BaseModel):
    description: str
    tags: Union[List[str], None] = None