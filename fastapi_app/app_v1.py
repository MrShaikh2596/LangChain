from fastapi import FastAPI
from routes import router


basic_app = FastAPI()
basic_app.include_router(router)