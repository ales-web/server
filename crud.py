from sqlalchemy.orm import Session

from models import Post
from schemas import PostCreate, PostUpdate


def get_all_posts(db: Session):
    return db.query(Post).all()


def get_post_by_id(id: int, db: Session):
    return db.get(Post, id)


def create_new_post(post: PostCreate, db: Session):
    post_to_create = Post(**post.model_dump())
    db.add(post_to_create)
    db.commit()
    db.refresh(post_to_create)
    return post_to_create


def update_existing_post(post: Post, new_post: PostUpdate, db: Session):
    post.name = new_post.name
    post.text = new_post.text
    db.commit()
    db.refresh(post)
    return post


def delete_existing_post(post: Post, db: Session):
    db.delete(post)
    db.commit()
