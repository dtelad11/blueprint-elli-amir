"""Tests for the /screener endpoint of the FastAPI backend."""

from fastapi.testclient import TestClient


import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from main import app


client = TestClient(app)


def test_screener_endpoint_returns_valid_structure():
    """
    Verify that the /screener endpoint returns the expected JSON structure.
    """
    response = client.get("/screener")
    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert "content" in data
    assert "display_name" in data["content"]
    assert "sections" in data["content"]
    assert isinstance(data["content"]["sections"], list)
    assert len(data["content"]["sections"]) > 0


