from db import SessionLocal, engine
from models import Base, Post
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from schemas import PostGet

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/posts", response_model=list[PostGet])
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()
