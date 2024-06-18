from contextlib import asynccontextmanager
from typing import Annotated
from db import sessionmanager
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
from sqlalchemy.ext.asyncio import AsyncSession

# Base.metadata.create_all(bind=engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


async def get_db_session():
    async with sessionmanager.session() as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


DBSessionDep = Annotated[AsyncSession, Depends(get_db_session)]

app = FastAPI(title="Ales backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/posts", response_model=PostsRead)
async def get_posts(db: DBSessionDep):
    posts = await get_all_posts(db)
    return {"posts": posts, "items": len(posts)}


@app.get("/posts/{id}", response_model=PostRead)
async def get_post(id: int, db: DBSessionDep):
    post = await get_post_by_id(id, db)
    if post == None:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    return post


@app.post("/posts", response_model=PostRead)
async def create_post(post: PostCreate, db: DBSessionDep):
    return await create_new_post(post, db)


@app.put("/posts/{id}", response_model=PostRead)
async def update_post(id: int, post: PostUpdate, db: DBSessionDep):
    post_to_update = await get_post_by_id(id, db)
    if post_to_update == None:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    return await update_existing_post(post_to_update, post, db)


@app.delete("/posts/{id}", status_code=200)
async def delete_post(id: int, db: DBSessionDep):
    post_to_delete = await get_post_by_id(id, db)
    if post_to_delete == None:
        return JSONResponse(status_code=404, content={"Message": "Not Found"})
    result = await delete_existing_post(post_to_delete, db)
    if result == False:
        return JSONResponse(status_code=404, content={"Message": "Not Found"})
