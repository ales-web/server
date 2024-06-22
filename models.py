from datetime import datetime

# from db import SQLBase
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


def get_time_utc():
    return datetime.utcnow()


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    text: Mapped[str]
    dateCreate: Mapped[datetime] = mapped_column(insert_default=get_time_utc)
    dateUpdate: Mapped[datetime] = mapped_column(
        insert_default=get_time_utc, onupdate=get_time_utc
    )
    picture: Mapped[str] = mapped_column(nullable=True)
    views: Mapped[int] = mapped_column(server_default="0")
