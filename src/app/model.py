from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Posts(Base):
    id = Column(String(length=10), primary_key=True)
    title = Column(String(length=100), nullable=False)
    content = Column(String(length=10000), default=None, nullable=True)
    created_at = Column(DateTime, nullable=True, default=datetime.now())
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    __tablename__ = "posts"