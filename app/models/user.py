from sqlalchemy import Integer,String,Column,DateTime
from datetime import datetime, UTC
from app.database.base import Base


class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True)
    username=Column(String(50),nullable=False,unique=True,index=True)
    email=Column(String(255),nullable=False,unique=True,index=True)
    created_at=Column(DateTime(timezone=True),nullable=False,default=lambda :datetime.now(UTC))
    hashed_password=Column(String(255),nullable=False)
