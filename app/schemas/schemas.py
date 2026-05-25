from pydantic import BaseModel, ConfigDict, AnyHttpUrl, field_validator, Field
from datetime import datetime
import re


class URLBase(BaseModel):
    original_url: AnyHttpUrl

class URLCreate(URLBase):
    expires_at : datetime | None = None
    custom_alias: str | None = Field(default=None, min_length=4, max_length=20)

    @field_validator('custom_alias')
    @classmethod
    def alias_is_valid(cls, v):
        if v is None:
            return v
        if not re.match(r'^[a-zA-Z0-9-]+$', v):
            raise ValueError('Custom alias can only contain letters, numbers, and hyphens')
        return v

class URLResponse(URLBase):
    model_config = ConfigDict(from_attributes=True)

    short_code: str
    created_at: datetime
    expires_at: datetime | None
    click_count: int
