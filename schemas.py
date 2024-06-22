from datetime import datetime
from pydantic import BaseModel


class PostCreate(BaseModel):
    name: str
    text: str
    picture: str | None = None
    views: int = 0


# id field must be on first place in documentation
class PostRead(BaseModel):
    id: int
    name: str
    text: str
    dateCreate: datetime
    dateUpdate: datetime
    picture: str | None
    views: int


class PostUpdate(PostCreate):
    name: str | None = None
    text: str | None = None


class PostsRead(BaseModel):
    posts: list[PostRead]
    items: int
