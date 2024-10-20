from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")

async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": "Hehe! This is the data!"}


@app.post("/createposts")
async def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"newpost":f"title {payload['title']} content : {payload['content']}"}
    