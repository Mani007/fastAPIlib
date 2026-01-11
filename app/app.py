import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

GCP = os.getenv('TEMPORARY')

app = FastAPI()


@app.get("/")
async def read_root():
    print(GCP)
    return {"Hello": "World"}