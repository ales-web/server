from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from models import Post
from schemas import PostCreate, PostUpdate


async def get_all_posts(db: AsyncSession):
    return (await db.scalars(select(Post))).all()


async def get_post_by_id(id: int, db: AsyncSession):
    return (await db.scalars(select(Post).where(Post.id == id))).first()


async def create_new_post(post: PostCreate, db: Session):
    post_to_create = Post(**post.model_dump())
    db.add(post_to_create)
    await db.commit()
    await db.refresh(post_to_create)
    return post_to_create


async def update_existing_post(post: Post, new_post: PostUpdate, db: Session):
    updated_post = new_post.model_dump(exclude_unset=True)
    for key, value in updated_post.items():
        setattr(post, key, value)
    await db.commit()
    await db.refresh(post)
    return post


async def delete_existing_post(post: Post, db: Session):
    await db.delete(post)
    await db.commit()
    if await get_post_by_id(post.id, db) == None:
        return True
    return False
