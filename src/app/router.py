from fastapi import APIRouter,Depends, status, Header
from sqlalchemy.orm import Session
from db import get_db
from schema import ResponseCreate, Response, PostBase, ResponsePostList

router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=Response)
def create_user(*, db: Session = Depends(get_db)):
    """
    유저 생성 API
    """


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=ResponseCreate)
def create(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    게시글 생성 API
    """


@router.delete("/posts/{id}", status_code=status.HTTP_200_OK, response_model=Response)
def delete(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    게시글 삭제 API
    """


@router.put("/posts/{id}", status_code=status.HTTP_200_OK, response_model=Response)
def delete(*, db: Session = Depends(get_db), authorization: str = Header(None)):
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