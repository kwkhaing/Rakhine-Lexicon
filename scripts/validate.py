
import json, os, sys
from jsonschema import validate, ValidationError

SCHEMA_PATH = "schema/lexicon-schema.json"
LEXICON_DIR = "lexicon"

def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_entries(schema):
    errors = 0
    for root, _, files in os.walk(LEXICON_DIR):
        for fn in files:
            if fn.endswith(".json"):
                path = os.path.join(root, fn)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    validate(data, schema)
                    print(f"[OK] {path}")
                except ValidationError as e:
                    print(f"[ERROR] {path}: {e.message}")
                    errors += 1
    return errors

if __name__ == "__main__":
    schema = load_schema()
    errors = validate_entries(schema)
    if errors:
        sys.exit(1)
    print("All entries validated successfully.")
