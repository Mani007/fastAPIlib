import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

temp_key = os.getenv('TEMPORARY')

app = FastAPI()


@app.get("/")
async def read_root():
    
    return {"Hello": "World"}