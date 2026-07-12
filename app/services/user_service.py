from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password


def create_user(
        db:Session,
        user: UserCreate
):
    hashed_password = hash_password(user.password)
    new_user=User(
        username=user.username,
        email=user.email, 
        hashed_password=hashed_password

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
    



def get_user_by_email(
        db:Session,
        email:str
):    
    return(
        db.query(User)
        .filter(User.email==email)
        .first()
    )

def get_user_by_id(
    db: Session,
    user_id: int
):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )