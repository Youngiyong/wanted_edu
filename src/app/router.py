from fastapi import APIRouter,Depends, status, Header
from sqlalchemy.orm import Session
from db import get_db

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
def create(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    게시글 생성 API
    """


@router.delete("", status_code=status.HTTP_200_OK)
def delete(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    게시글 삭제 API
    """


@router.put("", status_code=status.HTTP_200_OK)
def delete(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    게시글 수정 API
    """


@router.get("", status_code=status.HTTP_200_OK)
def get_list(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    전체 게시글 API
    """


@router.get("", status_code=status.HTTP_200_OK)
def get(*, db: Session = Depends(get_db), authorization: str = Header(None)):
    """
    특정 게시글 API
    """