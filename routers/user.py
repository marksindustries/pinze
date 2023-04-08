from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from fastapi.encoders import jsonable_encoder
from schemas import Posts

import models




router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/getUsers")
async def getUser(db:Session  = Depends(get_db)):
    all = db.query(models.Posting).all()
    return all

@router.post('/createPost')
async def createUser(post:Posts,db:Session = Depends(get_db)):
    new_post = models.Posting()
    new_post.post = jsonable_encoder(post.post)
    db.add(new_post)
    db.commit()
    return new_post

   