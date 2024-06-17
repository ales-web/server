from datetime import datetime
from pydantic import BaseModel


class PostCreate(BaseModel):
    name: str
    text: str


# id field must be on first place in documentation
class PostRead(BaseModel):
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
