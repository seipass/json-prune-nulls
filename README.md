# json-prune-nulls

JSON null pruner.

## Usage

Install with `pip install .`. Pipe input into `json-prune-nulls` or pass a file path. Structured JSON tools accept JSON on stdin; CSV tools accept CSV; text and URL tools accept plain text. Output is written to stdout.

```sh
printf '%s' '{"sample": 1}' | json-prune-nulls
python -m pytest
```

## Development

Python 3.9+. Run tests with `python -m pytest`. MIT licensed.
