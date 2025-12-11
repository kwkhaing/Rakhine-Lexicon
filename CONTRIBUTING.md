# Contributing Guidelines

Thank you for contributing to the Rakhine (rki) AI Lexicon!

## How to Add a New Word
1. Copy `schema/entry-template.json`
2. Fill out all fields
3. Save it under `lexicon/<first-letter>/<word>.json`
4. Run validation (script WIP)
5. Submit a pull request

## Sentence Contributions
- Add Rakhine sentences to: `corpus/community_submissions/pending/`
- For translations, use: `corpus/sentences_rki_eng.tsv`

## Rules
- Use Unicode Rakhine script (not Zawgyi)
- One JSON file per word
- Follow the schema exactly
