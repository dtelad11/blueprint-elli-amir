"""Loads and structures static data used by the API, such as the domain map."""

import json
from pathlib import Path


def load_diagnostic_screener(file_path: str = "data/blueprint_diagnostic_screener.json") -> dict:
    with open(Path(file_path), "r", encoding = "utf-8") as file:
        return json.load(file)


def load_domain_map(file_path: str = "data/domain_map.json") -> dict:
    with open(Path(file_path), "r", encoding = "utf-8") as file:
        data = json.load(file)
        # Convert list of dicts to a map from question_id to map.
        return {entry["question_id"]: entry["domain"] for entry in data}

