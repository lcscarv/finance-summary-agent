from fastapi import FastAPI
from src.api.routes import router


app = FastAPI()
app.title = "Finance Agent API"
app.include_router(router)
