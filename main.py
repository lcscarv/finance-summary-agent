from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import router


app = FastAPI()
app.title = "Finance Agent API"
app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for local dev. Restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
