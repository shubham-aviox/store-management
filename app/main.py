from fastapi import FastAPI, Request
import api, models
from db import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(api.router, prefix="/api", tags=[])