import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

temp_key = os.getenv('TEMPORARY')

app = FastAPI()

post = {
    "name":"abc",
    "age":25,
}
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/get_post")
async def get_posts():
    return post