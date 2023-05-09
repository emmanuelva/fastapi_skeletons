from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user, article

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)

models.Base.metadata.create_all(engine)
