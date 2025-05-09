import json
from pathlib import Path

def load_domain_map(file_path: str = "data/domain_map.json") -> dict:
    with open(Path(file_path), "r", encoding = "utf-8") as file:
        data = json.load(file)
        # Convert list of dicts to a map from question_id to map.
        return {entry["question_id"]: entry["domain"] for entry in data}

