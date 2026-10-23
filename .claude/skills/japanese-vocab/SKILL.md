---
name: japanese-vocab
description: Look up readings, English meanings, JLPT level, pitch accent and audio for a list of Japanese words using the Japanese Vocab Fetcher API (jisho, OJAD, Wadoku, Suzuki-kun, JapanesePod, Forvo, WaniKani, Tatoeba). Use when the user gives one or more Japanese words and wants translations, readings, pitch accent, example sentences, audio, or flashcard/vocab-list data.
---

# Japanese vocab lookup

Fetches information for a list of Japanese words from the Japanese Vocab Fetcher API
(`api/` in this repo, deployed at `https://api.benleong.uk/jp`) and condenses it.

## How to run

Use the bundled script (standard library only, works with any `python3`):

```bash
python3 .claude/skills/japanese-vocab/scripts/fetch_vocab.py 食べる 猫 静か
```

Words can also come from a file (one per line) or stdin, and may be separated by
commas or `、`:

```bash
python3 .claude/skills/japanese-vocab/scripts/fetch_vocab.py --file words.txt
echo "食べる、猫" | python3 .claude/skills/japanese-vocab/scripts/fetch_vocab.py
```

Options:

| Flag | Purpose |
| --- | --- |
| `--sources jisho,ojad` | Only query these sources. Default `jisho,ojad,suzuki,wadoku,japanesepod`; `all` adds `forvo,tatoeba,wanikani` (slower). |
| `--format json` | Condensed JSON instead of Markdown — use when you will post-process (e.g. building a CSV/Anki deck). |
| `--raw` | Full, unprocessed API response. |
| `--max-senses N` | Number of jisho senses to keep (default 3). |
| `--api-url URL` | Override the API (or set `VOCAB_API_URL`), e.g. `http://localhost:9090` for a local server started with `cd api && uv run python -m api.app`. |

The script sends words in batches of 20. Each request queries every source in
parallel and typically takes 5–15 seconds, so pick only the sources you need.

## Choosing sources

- Meanings / readings / JLPT → `jisho`
- Pitch accent → `ojad`, `wadoku` (dictionary entries), `suzuki` (Suzuki-kun, which
  predicts accent for any text, including conjugated forms and phrases)
- Audio URLs → `japanesepod` (fast), `forvo`, `wanikani`
- Example sentences → `tatoeba`, `wanikani`

## Reading the output

- **Pitch accent** uses `'` to mark the downstep: `たべ' る` means the pitch falls
  after `べ` (nakadaka); `ね' こ` falls after the first mora (atamadaka); `いぬ'` falls
  after the last mora (odaka). No `'` means heiban (no fall). When sources disagree,
  show all of them; OJAD and Wadoku are dictionary data, Suzuki-kun is a prediction.
- **jisho match** is shown when jisho's top result differs from the input word (e.g.
  for conjugated forms or typos) — mention this to the user.
- **⚠ source failed** lines mean that upstream source errored; the other sources are
  still valid. Don't retry repeatedly — just report what's missing.

Present the results to the user concisely (a table works well for several words),
and don't invent readings, meanings or accents the API didn't return.

## API reference

- `POST /words` with body `{"words": ["食べる", ...], "sources": ["jisho", "ojad"]}`
  (`sources` optional, defaults to all). Returns 400 on invalid input or unknown sources.
- `GET /words?words=<JSON-encoded list>` — original endpoint, always queries every
  source. The script falls back to this if the deployed API doesn't support POST yet.

Response: a list with one object per word, `{"word": ..., "<source>": {"success",
"error", "main_data"}}`. See `api/api/custom_types/response_types.py` for the shape of
each source's `main_data`.
