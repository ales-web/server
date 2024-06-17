from datetime import datetime
from pydantic import BaseModel


class PostGet(BaseModel):
    id: int
    name: str
    text: str
    dateCreate: datetime
    dateUpdate: datetime
