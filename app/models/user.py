from sqlalchemy import Integer,String,Column,DateTime
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime, UTC
from app.database.base import Base
from app.models.enums import UserRole


class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True)
    username=Column(String(50),nullable=False,unique=True,index=True)
    email=Column(String(255),nullable=False,unique=True,index=True)
    created_at=Column(DateTime(timezone=True),nullable=False,default=lambda :datetime.now(UTC))
    hashed_password=Column(String(255),nullable=False)
    role = Column(
    SQLEnum(
        UserRole,
        name="user_role",
        values_callable=lambda enum: [e.value for e in enum],
    ),
    nullable=False,
    default=UserRole.USER
    )

    cart = relationship(
        "Cart",
        back_populates="user",
        cascade="all, delete-orphan",
            uselist=False
    )

    orders = relationship(
    "Order",
    back_populates="user"
    )