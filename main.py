from fastapi import FastAPI,APIRouter
from routers import user
import models
from database import engine

app = FastAPI()



app.include_router(user.router)


models.Base.metadata.create_all(engine)