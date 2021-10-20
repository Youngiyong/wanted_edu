from fastapi import APIRouter,Depends, status, Header
from sqlalchemy.orm import Session
from db import get_db
from schema import ResponseCreate, Response, PostBase, ResponsePostList, RequestUser, UserBase
from crud import create_user
router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=ResponseCreate)
def post_user(*, db: Session = Depends(get_db), payload: RequestUser):
    """
    유저 생성 API
    """
    return create_user(db=db, payload=payload)


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=ResponseCreate)
def post(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    게시글 생성 API
    """


@router.delete("/posts/{id}", status_code=status.HTTP_200_OK, response_model=Response)
def delete(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    게시글 삭제 API
    """


@router.put("/posts/{id}", status_code=status.HTTP_200_OK, response_model=Response)
def put(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    게시글 수정 API
    """


@router.get("/posts", status_code=status.HTTP_200_OK, response_model=PostBase)
def get_list(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    전체 게시글 API
    """


@router.get("/posts/{id}", status_code=status.HTTP_200_OK, response_model=ResponsePostList)
def get(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    특정 게시글 API
    """