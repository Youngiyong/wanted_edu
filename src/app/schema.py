from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional, NewType
from uuid import UUID

UserID = NewType("UserID", UUID)


class RequestUser(BaseModel):
    email: str

    class Config:
        schema_extra = {
            "example": {
                "email": "youn9354@naver.com",
            }
        }


class UserBase(BaseModel):
    id: UserID
    email: str


class Post(BaseModel):
    id: int
    title: str
    content: str
    author: str
    created_at: datetime

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "제목",
                "content": "내용",
                "author": "윤기용",
                "created_at": "2021-10-20 16:30:00"
            }
        }


class PostBase(BaseModel):
    id: str
    title: str
    content: str
    author: str
    is_writer: bool
    created_at: datetime
    updated_at: datetime


class Response(BaseModel):
    code: str
    msg: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "code": "S000",
                "msg": "Success",
            }
        }


class ResponseCreate(BaseModel):
    code: str
    msg: str
    data: dict

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "code": "S000",
                "msg": "Success",
                "data": {
                    "id": 1
                }
            }
        }


class ResponsePostList(BaseModel):
    count: int
    data: List[Post] = []

    class Config:
        schema_extra = {
            "example": {
                "count": 2,
                "data": [
                    {
                        "id" : 1,
                        "title": "게시글 제목",
                        "content": "게시글 내용",
                        "author": "작성자",
                        "created_at": "2021-10-20 16:30:00",
                        "updated_at": "2021-10-20 16:30:00"
                    },
                    {
                        "id": 2,
                        "title": "게시글 제목2",
                        "content": "게시글 내용2",
                        "author": "작성자2",
                        "created_at": "2021-10-20 16:30:00",
                        "updated_at": "2021-10-20 16:30:00"
                    }
                ]
            }
        }


class RequestPost(BaseModel):
    title: str
    author: str
    content: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "게시글 제목",
                "content": "게시글 내용",
                "author": "작성자"
            }
        }


class RequestUpdatePost(BaseModel):
    title: Optional[str]
    content: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "게시글 제목 수정..",
                "content": "게시글 내용 수정..",
            }
        }