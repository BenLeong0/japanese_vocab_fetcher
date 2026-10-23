import base64
import json

import pytest  # type: ignore

from api import main


@pytest.fixture(name="get_info_calls")
def fixture_get_info_calls(monkeypatch):
    calls = []

    def fake_get_info(word_list, sources=None):
        calls.append((word_list, sources))
        return [{"word": word} for word in word_list]

    monkeypatch.setattr("api.main.get_info", fake_get_info)
    return calls


def make_post_event(body: str, is_base64: bool = False) -> dict:
    return {
        "requestContext": {"http": {"method": "POST"}},
        "body": body,
        "isBase64Encoded": is_base64,
    }


def test_post_words(get_info_calls):
    """
    - GIVEN a POST event with words and sources
    - WHEN the lambda handler is called
    - THEN check get_info is called with them and a 200 is returned
    """
    body = json.dumps({"words": ["食べる", " ", "猫 "], "sources": ["jisho"]})
    resp = main.lambda_handler(make_post_event(body), None)

    assert resp["statusCode"] == 200
    assert json.loads(resp["body"]) == [{"word": "食べる"}, {"word": "猫"}]
    assert get_info_calls == [(["食べる", "猫"], ["jisho"])]


def test_post_words_base64(get_info_calls):
    """
    - GIVEN a base64 encoded POST event body without sources
    - WHEN the lambda handler is called
    - THEN check the body is decoded and all sources are used
    """
    body = base64.b64encode(json.dumps({"words": ["猫"]}).encode()).decode()
    resp = main.lambda_handler(make_post_event(body, is_base64=True), None)

    assert resp["statusCode"] == 200
    assert get_info_calls == [(["猫"], None)]


@pytest.mark.parametrize(
    "body",
    [
        "not json",
        json.dumps(["猫"]),
        json.dumps({"words": "猫"}),
        json.dumps({"words": ["猫"], "sources": "jisho"}),
        json.dumps({"words": ["猫"], "sources": ["notasource"]}),
    ],
)
def test_post_words_bad_input(body):
    """
    - GIVEN an invalid POST body
    - WHEN the lambda handler is called
    - THEN check a 400 is returned
    """
    resp = main.lambda_handler(make_post_event(body), None)

    assert resp["statusCode"] == 400
    assert "error" in json.loads(resp["body"])
