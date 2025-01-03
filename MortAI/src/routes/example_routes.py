from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, PostgreSQL

router = APIRouter()

@router.get("/items/")
def get_items(db: Session = Depends(PostgreSQL.get_db)):
    items = db.query(models.Item).all()
    return items