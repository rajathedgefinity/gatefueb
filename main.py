import models

from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from models import User, Profile, Home, Tenant
from schemas import Usr, Prof, House

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
    User.is_active = usrmod.is_active
    User.is_admin = usrmod.is_admin
    db.add(user)
    db.commit()
    print(usrmod.email, usrmod.passwd, usrmod.is_active, usrmod.is_admin)
    return {'message': 'User Created'}


@app.get('/api/auth/fetch/{id}')
async def usr_fetch(id: int, db: Session = Depends(get_db)):
    """Creating a User and Storing a User Information"""

    user = db.query(User).filter_by(id=id)
    print(user)
    data = {
        'email': user[1].email,
        'password': user[1].passwd,
        'is_active': user[1].is_active,
        'is_admin': user[1].is_admin
    }
    return data
