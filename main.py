"""FastAPI application defining routes for the diagnostic screener and scoring logic."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from schemas import ScreenerSubmission, AssessmentResult
from data import load_diagnostic_screener, load_domain_map


app = FastAPI()
# Tell FastAPI to allow cross-origin requests. Not very elegant but good enough
# for the exercise.
app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "https://blueprint-elli-amir-ac8042d2a76d.herokuapp.com/",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)



# Load the diagnostic screener and domain map from the json file (... or
# database, or third-party API).
diagnostic_screener = load_diagnostic_screener()
domain_map = load_domain_map()


@app.get("/screener")
def get_diagnostic_screener():
    """
    Return the Blueprint Diagnostic Screener.
    """
    # Elli: For the purpose of the exercise, I'm taking a minimalistic
    # approach. In a real app we'd have a schema, validate contents, write
    # tests for this endpoint, et cetera.
    return diagnostic_screener


@app.post("/score", response_model=AssessmentResult)
def score_screener(submission: ScreenerSubmission):
    """
    Process a screener submission with patient's answers and return recommended Level-2 results.
    """
    # Make sure that all question ids belong to one of the domains.
    invalid_question_ids = [
        answer.question_id for answer in submission.answers
        if answer.question_id not in domain_map
    ]
    if invalid_question_ids:
        raise HTTPException(
            status_code=400,
            detail="Invalid question_ids(s): " + ', '.join(invalid_question_ids)
        )

    # Elli: Additional data validation could go here, for example, making sure
    # that all expected question IDs are present. If this logic grows, we
    # should extract it to a `validate_screener()` helper function.

    # Aggregate scores.
    scores = {}
    for answer in submission.answers:
        domain = domain_map.get(answer.question_id)
        scores[domain] = scores.get(domain, 0) + answer.value

    # Determine which Level-2 Assessments to assign based on each domain's score.
    # Elli: In a real app, this scoring logic would likely live in a separate
    # module or service layer, using some sort of dynamic data structure rather
    # than hard-coded strings.
    results = []
    if scores.get("depression", 0) >= 2:
        results.append("PHQ-9")
    if scores.get("mania", 0) >= 2:
        results.append("ASRM")
    if scores.get("anxiety", 0) >= 2:
        results.append("PHQ-9")
    if scores.get("substance_use") >= 1:
        results.append("ASSIST")

    return AssessmentResult(results = results)


# Mount the React app and serve it as default route. Not very elegant, but good
# enough for the exercise.
app.mount("/", StaticFiles(directory="frontend/dist/", html = True), name="frontend")


@app.get("/{full_path:path}")
def serve_frontend():
    return FileResponse(Path("frontend/dist/index.html"))


