from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.v1.endpoints.url_routers import api_router, redirect_router

Base.metadata.create_all(bind = engine)

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")
app.include_router(redirect_router)

@app.get('/health')
def check_health():
    return {"message": "healthy"}
