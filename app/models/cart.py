from sqlalchemy import Column, Integer,ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime,UTC
from app.database.base import Base


class Cart(Base):

    __tablename__ = "carts"

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    created_at= Column(DateTime(timezone=True),nullable= False,default= lambda : datetime.now(UTC))
    updated_at = Column(
    DateTime(timezone=True),
    nullable=False,
    default=lambda: datetime.now(UTC),
    onupdate=lambda: datetime.now(UTC)
    )
    
    user=relationship(
        "User",
        back_populates="cart"
    )
    items = relationship(
    "CartItem",
    back_populates="cart",
    cascade="all, delete-orphan"
    )


