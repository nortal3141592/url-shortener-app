from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.v1.endpoints.url_routers import api_router, redirect_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind = engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")
app.include_router(redirect_router)

@app.get('/health')
def check_health():
    return {"message": "healthy"}


