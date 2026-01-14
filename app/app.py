import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

temp_key = os.getenv('TEMPORARY')

app = FastAPI()

post ={
    "result": [
    {
        "id": 0,
        "name": "Vinson Shepard"
      },
      {
        "id": 1,
        "name": "Bishop Briggs"
      },
      {
        "id": 2,
        "name": "Jannie Cummings"
      }]
}
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/get_post")
async def get_posts():
    #return json.dumps(post)
    return post
  
@app.post("/add_post")
async def add_posts():
    #return json.dumps(post)
    post["result"].append({
        "id": 3,
        "name": "ABC"
      })
    return post