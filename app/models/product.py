from sqlalchemy import Column, Integer, String, Numeric,ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, default=0)
    
    category_id=Column(
        Integer,
        ForeignKey("categories.id")
    )
    category= relationship(
        "Category",
        back_populates="products"
    )

    