from pydantic import BaseModel
from typing import Optional


class Questions(BaseModel):
    questions:Optional[str]
    options:Optional[list[str]]
    answer:Optional[str]

class ImagePost(BaseModel):
    title:Optional[str]
    image:Optional[str]



class Source(BaseModel):
    typeOfPost:str
    imagePost : Optional[ImagePost]
    questionsPost:Optional[Questions]
    


class Posts(BaseModel):
    post:Source

    