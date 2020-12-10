# app.py
import requests
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI

class Website(BaseModel):
    url : str

app = FastAPI()

@app.get("/")
def home():
    return "Hello World"
  
@app.post('/elapsed/')
async def get_elapsed(website : Website):
    d = dict()
    d[website] = requests.get(website).total_seconds()
    return d
    
