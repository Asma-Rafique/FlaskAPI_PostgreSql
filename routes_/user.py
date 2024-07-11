from fastapi import Depends, APIRouter, HTTPException, status
# from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models.user
from sqlalchemy.orm import Session, joinedload
from schemas.user import User, UserLogin
from typing import List
from DB.template import SessionLocal, engine
from authentication_authorization_security.security import verify_password, hash_password
from authentication_authorization_security.jwt import create_access_token, timedelta, access_token_expire_date
user = APIRouter()
models.user.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user.post('/register')
async def create_user(user_detail: User, db: Session = Depends(get_db)):
    '''
    input user details
    return successful if user not already exist
    '''
    existing_user = db.query(models.user.UserModel).filter(
        models.user.UserModel.email == user_detail.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    userd = models.user.UserModel(username=user_detail.username,
                                  email=user_detail.email, password=hash_password(user_detail.password))
    db.add(userd)
    db.commit()
    db.refresh(userd)
    return {"msg": " User created successfully"}


@user.post('/login')
async def login(user_detail: UserLogin, db: Session = Depends(get_db)):
    """
    User login
    """
    db_user = db.query(models.user.UserModel).filter(
        models.user.UserModel.email == user_detail.email).first()
    if not db_user or not verify_password(user_detail.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=access_token_expire_date)
    access_token = create_access_token(
        data={"sub": db_user.email}, expires_delta=access_token_expires
    )
    return {"login": "successful", "access_token": access_token, "token_type": "bearer"}


@user.get('/users', response_model=List[User])
async def get_all_users(db: Session = Depends(get_db)):
    """
    Get all users
    """
    users = db.query(models.user.UserModel).all()
    return users


@user.get('/users/{username}', response_model=User)
async def get_user_by_username(username: str, db: Session = Depends(get_db)):
    """
    Get user by username
    """
    user = db.query(models.user.UserModel).filter(
        models.user.UserModel.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
