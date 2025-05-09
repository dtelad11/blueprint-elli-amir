# Blueprint Screener Exercise
## Elli Amir, el.ad.david.amir@gmail.com

### Live Demo

You can access the Heroku app at the following link:

[https://blueprint-elli-amir-ac8042d2a76d.herokuapp.com](https://blueprint-elli-amir-ac8042d2a76d.herokuapp.com)

### Problem Description

The task was to build a two-part application:

* A backend API to score responses to a clinical screener and assign follow-up
  assessments based on domain thresholds.
* A frontend UI that presents screener questions one-by-one and submits
  answers to the backend.

### Solution Overview

I coded the backend using Python and FastAPI. Static data (such as the domain
map) is loaded from JSON files. The `score_screener` function processes the
request body and returns the results.

Frontend is React and is hosted via FastAPI's static file support. Answers are
collected incrementally (maintaining the required format) and submitted to the
`/score` endpoint.

### Technical Choices

I chose this stack since I have prior experience setting it up on Heroku,
saving on DevOps time. FastAPI comes with Pydantic and Swagger UI, two tools
that make deployment faster and less error-prone. React is easy to iterate on,
which I find is especially crucial for frontend development.

In order to ease deployment, submission, and your review, I went for a single
repository, FastAPI's hosting, and JSON files for static data.


Describe how you would deploy this as a true production app on the platform of your choice:
How would ensure the application is highly available and performs well?
How would you secure it?
What would you add to make it easier to troubleshoot problems while it is running live?
Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend additional time on the project
Link to other code you're particularly proud of
Link to your resume or public profile

### LinkedIn

[https://www.linkedin.com/in/elli-el-ad-david-amir-68624b6/](https://www.linkedin.com/in/elli-el-ad-david-amir-68624b6/)

Thank you for your time and consideration!

