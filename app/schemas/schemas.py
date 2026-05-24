from pydantic import BaseModel, ConfigDict
from datetime import datetime

class URLBase(BaseModel):
    original_url: str

class URLCreate(URLBase):
    pass

class URLResponse(URLBase):
    model_config = ConfigDict(from_attributes=True)

    short_code: str
    created_at: datetime
    expires_at: datetime | None
