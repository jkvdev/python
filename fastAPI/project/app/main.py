from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Inventory API")
app.include_router(router)
