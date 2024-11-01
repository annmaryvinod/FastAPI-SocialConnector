from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


#using pydantic for schema validation
class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None
    
my_posts = [{"title": "title of post1","content":"content of post 1","id":1},
            {"title": "title of post2","content":"content of post 2","id":2},
            {"title": "title of post3","content":"content of post 3","id":3},
            {"title": "title of post4","content":"content of post 4","id":4}]
    
    

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.post("/posts")
async def create_posts(post : Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    print(my_posts)
    return {"data" : my_posts}
    