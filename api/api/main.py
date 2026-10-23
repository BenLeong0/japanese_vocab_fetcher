import base64
import json
import traceback

from api import utils
from api.coordinator import get_info

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
}


def make_response(status_code: int, body) -> dict:
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json", **CORS_HEADERS},
        "body": json.dumps(body),
    }


def lambda_handler(event, context):
    # REST API (v1) uses httpMethod; HTTP API (v2) uses requestContext.http.method
    method = event.get("httpMethod") or (
        event.get("requestContext", {}).get("http", {}).get("method")
    )
    if method == "OPTIONS":
        return {"statusCode": 204, "headers": CORS_HEADERS, "body": ""}

    if method == "POST":
        return handle_post(event)

    try:
        event["queryStringParameters"] = event.get("queryStringParameters") or {}
        word_list = utils.get_words_from_lambda(event)
        return make_response(200, get_info(word_list))
    except json.JSONDecodeError:
        return make_response(400, {"error": "'words' must be a JSON-encoded list"})
    except Exception:
        traceback.print_exc()
        return make_response(500, {"error": "Internal server error"})


def handle_post(event: dict) -> dict:
    """Handle POST /words, with body {"words": [...], "sources": [...]}"""
    try:
        raw_body = event.get("body") or "{}"
        if event.get("isBase64Encoded"):
            raw_body = base64.b64decode(raw_body).decode()
        word_list, sources = utils.parse_words_body(json.loads(raw_body))
        return make_response(200, get_info(word_list, sources))
    except json.JSONDecodeError:
        return make_response(400, {"error": "Body must be valid JSON"})
    except ValueError as e:
        return make_response(400, {"error": str(e)})
    except Exception:
        traceback.print_exc()
        return make_response(500, {"error": "Internal server error"})
