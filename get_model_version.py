import json
from pathlib import Path

META_PATH = Path(__file__).resolve().parent / "custom_spacy_model" / "meta.json"

def get_model_version() -> str:
    with META_PATH.open() as f:
        data = json.load(f)
    return data.get("version", "")

if __name__ == "__main__":
    print(get_model_version())
