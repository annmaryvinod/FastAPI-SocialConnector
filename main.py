from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": "Hehe! This is the data!"}
    