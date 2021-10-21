from fastapi import APIRouter,Depends, status, Header
from sqlalchemy.orm import Session
from db import get_db
from schema import ResponseCreate, Response, PostBase, ResponsePostList, RequestUser, RequestPost, RequestUpdatePost
from crud import create_user, create_post, delete_post, put_post, get_post, list_post
router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=ResponseCreate)
def post_user(*, db: Session = Depends(get_db), payload: RequestUser):
    """
    유저 생성 API
    """
    return create_user(db=db, payload=payload)


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=ResponseCreate)
def post(*, db: Session = Depends(get_db), user_id: str = Header(None), payload: RequestPost):
    """
    게시글 생성 API
    """
    return create_post(db=db, user_id=user_id, payload=payload)


@router.delete("/posts/{id}", status_code=status.HTTP_200_OK, response_model=Response)
def delete(*, db: Session = Depends(get_db), user_id: str = Header(None), id: str):
    """
    게시글 삭제 API
    """
    return delete_post(db=db, user_id=user_id, post_id=id)


@router.put("/posts/{id}", status_code=status.HTTP_200_OK, response_model=Response)
def put(*, db: Session = Depends(get_db), user_id: str = Header(None), id: str, payload: RequestUpdatePost):
    """
    게시글 수정 API
    """
    return put_post(db=db, user_id=user_id, post_id=id, payload=payload)


@router.get("/posts", status_code=status.HTTP_200_OK, response_model=ResponsePostList, response_model_exclude=["user_id", "deleted_at"])
def get_list(*, db: Session = Depends(get_db)):
    """
    전체 게시글 API
    """
    return list_post(db=db)


@router.get("/posts/{id}", status_code=status.HTTP_200_OK, response_model=PostBase)
def get(*, db: Session = Depends(get_db), user_id: str = Header(None), id: str):
    """
    특정 게시글 API
    """
    return get_post(db=db, post_id=id, user_id=user_id)
