from db import SessionLocal, engine
from models import Base, Post
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from schemas import PostRead, PostsRead, PostCreate, PostUpdate
from fastapi.responses import JSONResponse
from crud import (
    create_new_post,
    delete_existing_post,
    get_all_posts,
    get_post_by_id,
    update_existing_post,
)
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title="Ales backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/posts", response_model=PostsRead)
def get_posts(db: Session = Depends(get_db)):
    posts = get_all_posts(db)
    return {"posts": posts, "items": len(posts)}


@app.get("/posts/{id}", response_model=PostRead)
def get_post(id: int, db: Session = Depends(get_db)):
    post = get_post_by_id(id, db)
    if post == None:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    return post


@app.post("/posts", response_model=PostRead)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return create_new_post(post, db)


@app.put("/posts/{id}", response_model=PostRead)
def update_post(id: int, post: PostUpdate, db: Session = Depends(get_db)):
    post_to_update = get_post_by_id(id, db)
    if post_to_update == None:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    return update_existing_post(post_to_update, post, db)


@app.delete("/posts/{id}", status_code=200)
def delete_post(id: int, db: Session = Depends(get_db)):
    post_to_delete = get_post_by_id(id, db)
    if post_to_delete == None:
        return JSONResponse(status_code=404, content={"Message": "Not Found"})
    return delete_existing_post(post_to_delete, db)
