import json
from typing import Any

import uvicorn
from fastapi import Body, FastAPI, HTTPException
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


@app.post("/words")
async def post_words(body: Any = Body(...)):  # noqa: B008
    """
    Fetch information for a list of words, optionally restricted to some sources.
    Body: {"words": ["食べる", ...], "sources": ["jisho", "ojad"]}
    """
    try:
        word_list, sources = utils.parse_words_body(body)
        return get_info(word_list, sources)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


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
