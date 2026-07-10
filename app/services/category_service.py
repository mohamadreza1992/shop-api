from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate


def create_category(
    db: Session,
    category: CategoryCreate
):
    new_category = Category(
        name=category.name
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


def get_categories(db: Session):
    return db.query(Category).all()


def get_category_by_id(
    db: Session,
    category_id: int
):
    return (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )


def delete_category(
    db: Session,
    category_id: int
):
    category = (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )

    if category:
        db.delete(category)
        db.commit()
        return True

    return False