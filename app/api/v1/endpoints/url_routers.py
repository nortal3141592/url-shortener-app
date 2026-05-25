from typing import Annotated
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import RedirectResponse
from app.schemas.schemas import URLResponse, URLCreate
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.models import models
from app.core.utils import generate_short_code
from datetime import datetime, UTC

api_router = APIRouter()
redirect_router = APIRouter()

@api_router.post('/urls', response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def create_short_url(db: Annotated[Session, Depends(get_db)], input_url: URLCreate):
    if input_url.custom_alias is not None:
        if db.query(models.URL).filter(models.URL.short_code == input_url.custom_alias).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This custom alias is used by someone else, try again")
        short_code = input_url.custom_alias
    
    else:
        short_code = generate_short_code()
        while db.query(models.URL).filter(models.URL.short_code == short_code).first():
            short_code = generate_short_code()

    
    new_url = models.URL(
        original_url = str(input_url.original_url),
        short_code = short_code,
        expires_at = input_url.expires_at
    )
    
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url

@redirect_router.get('/{short_code}')
def redirect_to_url(short_code: str, db: Annotated[Session, Depends(get_db)]):
    result = db.query(models.URL).filter(models.URL.short_code == short_code)

    url = result.first()

    if not url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL doesn't exist")
    
    if url.expires_at is not None and url.expires_at < datetime.now():
        raise HTTPException(status_code=status.HTTP_410_GONE, detail="Url no longer exists")
    
    url.click_count += 1
    db.commit()
    db.refresh(url)
    
    return RedirectResponse(url.original_url)

@api_router.get('/urls/{short_code}', response_model=URLResponse)
def get_url_info(short_code:str, db: Annotated[Session, Depends(get_db)]):
    url = db.query(models.URL).filter(models.URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="url info not found")
    
    return url
