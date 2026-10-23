---
name: vocab-sheet
description: Add Japanese words to Ben's Anki vocab Google Sheet ("Japanese vocab" spreadsheet, tabs "Sentences" and "Custom Words"). Use this whenever the user gives one or more Japanese words and wants them added, put in, or logged to the spreadsheet / vocab sheet / sheet / Anki list — even if they just paste a word and say "add this", or paste a list of words from Notion. Looks up reading, meaning, pitch accent and an example sentence via the Japanese Vocab Fetcher API, formats the row the way the sheet's existing rows are formatted, checks for duplicates, and writes it with the Google Sheets connector. Not for one-off word lookups with no spreadsheet involved (use japanese-vocab for that).
---

# Add words to the vocab spreadsheet

The user keeps a Google Sheet of Japanese vocab that feeds an Anki deck. Given a
word (or a list of words), look each one up, build a row in the sheet's house
style, and write it to the right tab. The two things that matter most: don't
write a word that's already somewhere in the sheet, and match the existing
formatting exactly, because the rows are imported into Anki as-is.

## The spreadsheet

ID: `1isPsYd9ALwaUSnPwoyjI6zN_4FDvlvIN46l60yWL5F0` (Google Sheets connector).

| Tab | Purpose | Columns | Where new rows go |
| --- | --- | --- | --- |
| `Sentences` | Words that have an example sentence | B 助詞 · C Word · D Pronunciation · E Meaning · F Sentence (jp) · G Sentence (en) · H Notes | Directly under the last filled row (data starts at row 5) |
| `Custom Words` | Words with no sentence | Left block B–F = "Already added" (leave alone). Right block **H–L = "Not yet added"**: H 助詞 · I Word · J Pronunciation · K Meaning · L Notes | Directly under the last filled row of column I (data starts at row 5) |
| `N1 Vocab`, `N2 Vocab` | JLPT lists (never write here) | Word in column C | — |

Column A is always empty and column B / H (助詞) is the user's own — it holds
`x` marks for cards already imported into Anki, and occasionally a particle.
Never write to A, B or H, and never clear or move an existing `x`.

A word goes to `Sentences` if a good example sentence exists or you can
confidently write one; otherwise to `Custom Words`. Prefer `Sentences`: proverbs,
set phrases and rare technical nouns are the usual `Custom Words` cases.

## Workflow

### 1. Collect the words

Accept one word or many: space/comma/`、`/newline separated, a pasted Notion
table, or a list with readings and sentences attached. If the user supplies
their own sentence, reading or definition for a word, that takes priority over
anything the API returns (fix obvious typos in their sentence and say so).
Strip bracketed notes like `くぐる (to pass through)` down to the word but keep
the hint for choosing the sense.

### 2. Check for duplicates

Read just the Word columns — full-range reads of these tabs overflow the tool
output limit:

```
Sentences!C5:C3000     Custom Words!C5:C2000     Custom Words!I5:I2000
N1 Vocab!C5:C2000      N2 Vocab!C5:C2000
```

Compare after stripping `（する）`-style suffixes and splitting on `・` / `/`
(e.g. `中身・中味`). A match in any tab means skip the word and tell the user
where it already is. Treat alternative spellings as duplicates too when you
notice them (お出かけ vs お出掛け, 率直 vs 卒直) and mention it.

### 3. Look the words up

```bash
python3 <this skill>/scripts/lookup.py 蝉 蜻蛉
python3 <this skill>/scripts/lookup.py --file words.txt
```

This calls the API one word at a time (multi-word requests return 500 on the
deployed API), with retries, and prints compact JSON: readings, senses with
parts of speech, `suru_verb` and `usually_kana` flags, OJAD accent and up to
five Tatoeba sentences. Default sources are `jisho,ojad,tatoeba`; add `wadoku`
for a second accent opinion. Expect ~10–20 s per word, so run lists of more
than a handful in the background (`run_in_background`) and keep working.
A source listed under `errors` just failed upstream — don't retry it more than
once; report the gap instead.

If jisho matches a different headword (`jisho_match` ≠ word), the user's
spelling is a variant or the word is usually written in kana. Keep the user's
spelling in the Word column and put the dictionary form in Notes when it's
useful (e.g. `Also written 冷や奴`). A kana-only input with no match usually
has a kanji form — try it (へばりつく → へばり付く) but keep the kana as the
Word, since that's what the user will see on the card.

### 4. Build the row

Match the existing rows exactly; open a few recent ones if in doubt.

**Word (C / I)**
- The word as the user wrote it. Append `（する）` when jisho tags a sense
  `Suru verb` or the word is plainly used with する (休日出勤, 追いかけっこ).
- Mimetic/adverbial words that take と and する get `（と・する）`
  (にっこり（と・する）); と only → `（と）`; に only → `（に）`.
- Two readings with different meanings become two rows, disambiguated
  `退ける【ど】` / `退ける【しりぞ】`.

**Pronunciation (D / J)**
- Hiragana (katakana for loanword parts: てっきんコンクリート).
- Pitch accent only from OJAD/Wadoku; mark the downstep with `'` followed by a
  space after the mora it falls on: `たべ' る`, `さ' る`, `きりはな' す`. Odaka
  (fall after the last mora) is a trailing `'` with no space: `つぼみ'`. Heiban
  has no mark. If the API returned no accent, leave the reading bare — never
  invent one.
- Alternative readings joined with `・`: `しょいこむ・せおいこむ`. Several OJAD
  accents for the same reading are listed the same way: `ものお' と・ものおと'`.

**Meaning (E / K)**
- Capitalise the first letter of each gloss, British spelling (Colour, Mould,
  Favouritism).
- Synonyms within one sense: ` ; ` (space-semicolon-space).
  Separate senses: `  /  ` (two spaces, slash, two spaces).
  Example: `Billiards ; Pool  /  Serial collisions (of cars)`.
- Keep 1–4 glosses per sense and only the senses worth learning; drop
  Wikipedia-definition senses and place names.
- Qualifiers go in parentheses inside the gloss: `(eg a flag)`, `(usu. kana)`,
  `(tr.)` / `(intr.)` when transitivity is the point, `(variant of 悲しい)`.
- Verbs start with `To …`.

**Sentence (F, G) — Sentences tab only**
Priority order:
1. A sentence the user supplied (book quote, Notion card). Translate it if it
   has no English.
2. A Tatoeba sentence that uses the target word naturally in the sense being
   taught, is a complete sentence, and isn't crude or oddly technical. The
   first Tatoeba hit is often not the best — read all five.
3. One you write yourself, only for everyday words where you're sure of the
   collocation. Keep it short and plain; mention in the reply which ones you
   wrote so the user can review them.
If none of these gives a sentence you'd stand behind, the word goes to
`Custom Words` instead.

**Notes (H / L)** — usually empty. Use it for a kanji form of a kana word, an
alternative spelling, or a reading warning. Don't copy source references
(page numbers, episode names) unless asked.

### 5. Write the rows

1. Find the next row: read `Sentences!C<last known>:C<+50>` (or
   `Custom Words!I…`) and take the row after the last non-empty cell. Confirm
   the target cells are empty with a second small read — the tabs have blank
   rows below the data, so `append_values` can land in the wrong place.
2. Write with `update_values` to an explicit range starting at column C
   (Sentences) or I (Custom Words), e.g. `Sentences!C1390:H1391`, so columns
   A/B/H stay untouched. Rows are `[word, reading, meaning, jp, en, notes]`
   or `[word, reading, meaning, notes]`.
3. Read the written range back once to confirm.

### 6. Reply

Short. A table of what was added (word, reading, meaning, which tab), then
one line each for: words skipped as duplicates (and where), sentences you
wrote yourself, accent gaps, and anything you guessed (sense choice, spelling
normalisation, `（する）` added on your own judgment). If a word couldn't be
found at all, say so and ask rather than inventing an entry.

## Example

Input: `add 冷奴`

Lookup → reading ひややっこ, jisho match 冷や奴, "cold tofu (served with
condiments)", no OJAD accent, no Tatoeba sentence. Duplicate check: not in any
tab. Everyday food word, so write a sentence:

| C | D | E | F | G | H |
| --- | --- | --- | --- | --- | --- |
| 冷奴 | ひややっこ | Hiyayakko ; Cold tofu (served with condiments) | 夏はやっぱり冷奴に限る。 | In summer, nothing beats hiyayakko. | Also written 冷や奴 |

Reply: the row as a table, plus "sentence is mine; no OJAD accent available".
