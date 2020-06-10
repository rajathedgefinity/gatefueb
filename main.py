import models

from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from models import User, Profile, Home, Tenant

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
    return {'ping': 'pong'}
