"""Defines Pydantic models used for request and response validation."""
from pydantic import BaseModel, conint
from typing import List


class Answer(BaseModel):
    question_id: str
    value: conint(ge=0, le=4)


class ScreenerSubmission(BaseModel):
    answers: List[Answer]


class AssessmentResult(BaseModel):
    results: list[str]


