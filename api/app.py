import json
import random
import uvicorn
import logging
from enum import Enum
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from words import words


app = FastAPI()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

class Lang(str, Enum):
    fr = "fr"
    en = "en"
    es = "es"

@app.get("/word/generate")
def generate_word(
    lenght: int=Query(
        title="Lenght of the generate word",
        ge=4, le=12, default=8),
    lang: Lang=Query(
        title="Language of the generate word",
        default=Lang.fr
    )):
    logging.debug("test")
    return {"word": random.choice(words[lang][lenght])}

@app.get("/word/hello")
def hello():
    return {"hello": "world"}

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
