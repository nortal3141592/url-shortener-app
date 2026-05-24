from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.v1.endpoints.urls import router

Base.metadata.create_all(bind = engine)

app = FastAPI()
app.include_router(router, prefix="/api/v1")

@app.get('/health')
def check_health():
    return {"message": "healthy"}
