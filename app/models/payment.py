from sqlalchemy import (
    Integer,
    String,
    Column,
    ForeignKey,
    DateTime,
    Numeric
)
from sqlalchemy.orm import relationship
from datetime import datetime, UTC

from app.database.base import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders.id"),
        nullable=False,
        unique=True
    )

    amount = Column(
        Numeric(10,2),
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False,
        default="pending"
    )

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )


    order = relationship(
        "Order",
        back_populates="payment"
    )