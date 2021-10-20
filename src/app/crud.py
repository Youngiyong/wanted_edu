from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from model import Posts, Users
from schema import RequestUser
import uuid
from datetime import datetime, timedelta


def create_user(db: Session, payload: RequestUser):
    # 유저 중복 체크
    user = db.query(Users).filter(Users.email==payload.email).first()

    if user:
        raise HTTPException(status_code=400, detail="유저가 이미 존재합니다.")

    user = Users(id=str(uuid.uuid4()), email=payload.email)
    db.add(user)
    db.commit()
    return {"code": "S0000", "msg": "Success", "data" : {"id" : user.id}}
