"""Tests for the /score endpoint of the FastAPI backend."""

from fastapi.testclient import TestClient


import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from main import app


client = TestClient(app)


def test_score_endpoint_returns_expected_assessments():
    """
    Send a valid screener submission and check that the returned assessments
    match the expected results.
    """
    submission = {
        "answers": [
            {"value": 1, "question_id": "question_a"},
            {"value": 1, "question_id": "question_b"},
            {"value": 1, "question_id": "question_c"},
            {"value": 1, "question_id": "question_d"},
            {"value": 1, "question_id": "question_e"},
            {"value": 0, "question_id": "question_f"},
            {"value": 0, "question_id": "question_g"},
            {"value": 1, "question_id": "question_h"}
        ]
    }

    response = client.post("/score", json=submission)
    assert response.status_code == 200

    result = response.json()
    assert "results" in result

    expected_result = {"PHQ-9", "ASRM", "ASSIST"}
    assert set(result["results"]) == expected_result


def test_score_endpoint_returns_invalid_question_ids():
    """
    Send a screener submission with invalid question IDs and check that the
    endpoint returns an exception.
    """
    submission = {
        "answers": [
            {"value": 1, "question_id": "question_a"},
            {"value": 1, "question_id": "question_a_invalid"},
            {"value": 1, "question_id": "question_b"},
            {"value": 1, "question_id": "question_b_invalid"}
        ]
    }

    response = client.post("/score", json=submission)
    assert response.status_code == 400

    result = response.json()
    assert "detail" in result
    assert result["detail"] == "Invalid question_id(s): question_a_invalid, question_b_invalid"


