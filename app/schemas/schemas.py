from pydantic import BaseModel, ConfigDict, AnyHttpUrl
from datetime import datetime

class URLBase(BaseModel):
    original_url: AnyHttpUrl

class URLCreate(URLBase):
    expires_at : datetime | None = None

class URLResponse(URLBase):
    model_config = ConfigDict(from_attributes=True)

    short_code: str
    created_at: datetime
    expires_at: datetime | None
