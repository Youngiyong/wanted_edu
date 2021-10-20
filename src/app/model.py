from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    id = Column(String(length=100), primary_key=True)
    email = Column(String(length=100), nullable=False)
    __tablename__ = "users"


class Posts(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), nullable=False)
    author = Column(String(length=100), nullable=False)
    user_id = Column(String(length=255), nullable=False)
    content = Column(String(length=1000), default=None, nullable=True)
    created_at = Column(DateTime, nullable=True, default=datetime.now())
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    __tablename__ = "posts"