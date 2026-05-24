from typing import Annotated
from fastapi import APIRouter, status, Depends
from app.schemas.schemas import URLResponse, URLCreate
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.services.url_service import create_short_url

router = APIRouter()

@router.post('/urls', response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def create_url(db: Annotated[Session, Depends(get_db)], input_url: URLCreate):
    return create_short_url(db, input_url)
