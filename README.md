# Japanese Vocab Fetcher

## Overview

A web app to quickly fetch translations and pitch accent information for lists of Japanese
vocabulary. Consists of a UI built in React, and a backend Python Flask server (hosted on AWS).

Fetches information from [jisho.org](jisho.org), [Wadoku](wadoku.de) and Tokyo
University's OJAD ([Suzuki-kun](http://www.gavo.t.u-tokyo.ac.jp/ojad/eng/phrasing/index) and
[Word Search](http://www.gavo.t.u-tokyo.ac.jp/ojad/search)), and audio files from
[Forvo](forvo.com) and [Wanikani](wanikani.com).

Potential project extensions:
- Caching service
- Database to save searches


## Data flow

The first page of the UI will simply be a text input box, where a list of Japanese words can be
input (separated by newlines), or a text file containing the words can be uploaded.

The web app will send the list to the backend as a JSON encoded array of strings.

The backend will validate the input, then send (multithreaded) HTTP requests to all the information
sources. Audio files will just return URLs to where they are hosted on Forvo/Wanikani. The response
will be of the following form, JSON encoded:

```
[
  {
    "word": "食べる",
    "jisho": {
      "success": true,
      "error": null,
      "main_data": {
        "results": [
          {
            "slug": "食べる",
            "is_common": true,
            "tags": ["wanikani6"],
            "jlpt": ["jlpt-n5"],
            "japanese": [{"word": "食べる", "reading": "たべる"}, ...],
            "senses": [
              {
                "english_definitions": [ ... ],
                "parts_of_speech": [ ... ],
                "links": [ ... ],
                "tags": [ ... ],
                "restrictions": [ ... ],
                "see_also": [ ... ],
                "antonyms": [ ... ],
                "source": [ ... ],
                "info": [ ... ]
              },
              ...
            ],
            "attribution": {
              "jmdict": True,
              "jmnedict": False,
              "dbpedia": False
            },
          },
          ...
        ],
        "extra": [
          {
            "slug": "食べるラー油",
            "japanese": [{"word": "食べるラー油", "reading": "たべるラーゆ"}, ...]
          },
          ...
        ]
    }
    "ojad": {
      "success": true,
      "error": null,
      "main_data": {
        "accent": ["たべ' る"],
      },
    },
    "suzuki": {
      "success": true,
      "error": null,
      "main_data": {
        "accent": ["たべ' る"],
      },
    },
    "wadoku": {
      "success": true,
      "error": null,
      "main_data": {
        "accent": ["たべ' る"],
      },
    },
    "forvo": {
      "success": true,
      "error": null,
      "main_data": {
        "audio": [{...}, ...],
      },
    },
    "wanikani" {
      "success": true,
      "error": null,
      "main_data": {
        "audio": [{...}, ...],
        "sentences": [{"en": ..., "jp": ...,}, ...],
      },
    }
  },
  ...
]
```

In the case of an error in a module, `success` will be set to `false`, and `error` will be an object containing information about the error. `main_data` will maintain its structure, but will be empty. For example:
```
[
  {
    "word": "badinput",
    "jisho": {
      "success": false,
      "error": {
        "status_code": 500,
        "error_msg": "Internal server error",
        "url": "https://jisho.org/api/v1/search/words?keyword=badinput",
      }
      "main_data": {
        "results": [],
        "extra": [],
      },
    },
    ...
  },
  ...
]
```
