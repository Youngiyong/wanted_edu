from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from model import Posts, Users
from schema import RequestUser, RequestPost, RequestUpdatePost
import uuid
from datetime import datetime, timedelta


def put_post(db: Session, user_id: str, post_id: str, payload: RequestUpdatePost):
    post = db.query(Posts).filter(Posts.id==post_id,
                                  Posts.user_id==user_id,
                                  Posts.deleted_at==None).first()
    if post is None:
        raise HTTPException(status_code=404, detail="존재하지 않는 포스트이거나 권한이 없는 사용자입니다.")

    for key in payload.dict():
        setattr(post, key, payload.dict().get(key))
        print(payload.dict().get(key))
    post.updated_at = datetime.now()
    db.add(post)
    db.commit()

    return {"code": "S0000", "msg": "Success", "data": post}


def get_post(db: Session, post_id: str, user_id: str):
    post = db.query(Posts).filter(Posts.id==post_id,
                                  Posts.deleted_at==None).first()
    if post is None:
        raise HTTPException(status_code=404, detail="존재하지 않는 포스트입니다.")

    res = {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author,
        "is_writer": True if post.user_id == user_id else False,
        "created_at": post.created_at,
        "updated_at": post.updated_at
    }
    return res


def delete_post(db: Session, user_id: str, post_id: str):
    post = db.query(Posts).filter(Posts.id==post_id,
                                  Posts.user_id==user_id,
                                  Posts.deleted_at==None).first()
    if post is None:
        raise HTTPException(status_code=404, detail="존재하지 않는 포스트이거나 권한이 없는 사용자입니다.")

    post.updated_at = datetime.now()
    post.deleted_at = datetime.now()
    db.add(post)
    db.commit()
    return {"code": "S0000", "msg": "Success"}


def create_post(db: Session, user_id: str, payload: RequestPost):
    user = db.query(Users).filter(Users.id==user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="존재하지 않는 유저입니다.")
    post = Posts(user_id=user_id,
                 title=payload.title,
                 content=payload.content,
                 author=payload.author)
    db.add(post)
    db.commit()
    return {"code": "S0000", "msg": "Success", "data": {"id": post.id}}


def create_user(db: Session, payload: RequestUser):
    user = db.query(Users).filter(Users.email==payload.email).first()

    if user:
        raise HTTPException(status_code=404, detail="유저가 이미 존재합니다.")

    user = Users(id=str(uuid.uuid4()), email=payload.email)
    db.add(user)
    db.commit()
    return {"code": "S0000", "msg": "Success", "data": {"id": user.id}}


def list_post(db: Session):
    post = db.query(Posts).filter(Posts.deleted_at == None).all()

    res = {
        "count": "3",
        "data": post
    }
    return res
