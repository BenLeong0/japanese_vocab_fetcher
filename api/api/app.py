import json

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import utils
from api.coordinator import get_info

app = FastAPI(title="app", openapi_url="/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/words")
async def homepage(words: str):
    return get_info(json.loads(words))


def lambda_handler(event, context):
    word_list = utils.get_words_from_lambda(event)
    resp = get_info(word_list)
    return resp


if __name__ == "__main__":
    uvicorn.run(
        "api.app:app",
        host="0.0.0.0",
        port=9090,
        reload=True,
    )
