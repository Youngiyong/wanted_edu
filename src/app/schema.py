from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional


class PostBase(BaseModel):
    id: str
    title: str
    content: str
    author: str
    created_at: datetime
    updated_at: datetime


class Response(BaseModel):
    code: str
    msg: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "msg": "Success",
                "code": "S000",
            }
        }


class ResponsePostList(BaseModel):
    count: int
    data:  Optional[List[PostBase]]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "count": 2,
                "data":[
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


class RequestCreatePost(BaseModel):
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