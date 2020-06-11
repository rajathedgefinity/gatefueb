import models

from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from models import User, Profile, Home, Tenant
from schema import Usr, Prof, House

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/')
async def ping(db: Session = Depends(get_db)):
    """ Testing Application and DB Connection!"""
    return {'ping': 'pong'}


@app.post('/api/auth/add')
async def usr_add(usrmod: Usr, db: Session = Depends(get_db)):
    """Creating a User and Storing a User Information"""

    user = User()

    user.email = usrmod.email
    user.hashed_password = usrmod.passwd
    user.is_active = bool(usrmod.is_active)
    user.is_admin = bool(usrmod.is_admin)

    db.add(user)
    db.commit()

    return {'message': 'User Created'}


@app.get('/api/auth/fetch/{id}')
async def usr_fetch(id: int, db: Session = Depends(get_db)):
    """Creating a User and Storing a User Information"""

    user = db.query(User).filter(User.id == id).first()

    data = {
        'email': user.email,
        'password': user.hashed_password,
        'is_active': user.is_active,
        'is_admin': user.is_admin
    }

    return data
