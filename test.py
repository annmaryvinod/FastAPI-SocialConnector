from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = False
    rating : Optional[int] = None
    
myposts = [{"title":"title of 1st blog","content":"content of post 1","id":1}]
    
@app.get('/')
async def root():
    return {"message" : "this is the root file"}

@app.get('/posts')
async def getposts():
    return {"data" : myposts}

@app.post('/posts')
async def createpost(post:Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0,10000000)
    myposts.append(post_dict)
    return{"data" : myposts}
    