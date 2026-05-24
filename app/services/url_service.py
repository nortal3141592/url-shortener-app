from app.core.utils import generate_short_code
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import models
from app.schemas.schemas import URLCreate

def create_short_url(db: Session, input_url: URLCreate) -> models.URL:
    short_code = generate_short_code()

    while db.query(models.URL).filter(models.URL.short_code == short_code).first():
        short_code = generate_short_code()

    new_url = models.URL(
        original_url = input_url.original_url,
        short_code = short_code,
        expires_at = input_url.expires_at
    )
    
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url