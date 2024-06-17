from datetime import datetime
from pydantic import BaseModel


class PostCreate(BaseModel):
    name: str
    text: str


class PostRead(PostCreate):
    id: int
    name: str
    text: str
    dateCreate: datetime
    dateUpdate: datetime


class PostUpdate(PostCreate):
    pass


class PostsRead(BaseModel):
    posts: list[PostRead]
    items: int
