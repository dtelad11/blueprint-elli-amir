# Blueprint Screener Exercise
## Elli Amir, el.ad.david.amir@gmail.com

### Live Demo

[https://blueprint-elli-amir-ac8042d2a76d.herokuapp.com](https://blueprint-elli-amir-ac8042d2a76d.herokuapp.com)

### Problem Description

Build a two-part application:

- A backend API to score responses to a clinical screener and recommend follow-up assessments based on domain thresholds.
- A frontend UI that presents questions one at a time, collects user responses, and submits them to the backend in a specified format.

### Solution Overview

The backend is written in Python with FastAPI, using Pydantic models for input validation. Static data (such as the domain map) is stored as JSON and loaded at runtime. The `/score` endpoint calculates domain scores and returns a list of recommended assessments.

The frontend is built with React, and is served as static content via FastAPI. Users progress through the screener one question at a time, with responses submitted to the backend upon completion.

### Technical Choices

Full disclosure, I chose this stack since I have prior experience setting it up on Heroku, saving on DevOps time. With that said:

FastAPI comes with Pydantic and Swagger UI, two tools that make prototyping, ongoing support, and deployment faster and less error-prone. React is easy to iterate on, which I find is especially crucial for frontend development.

In order to ease deployment, submission, and your review, I went for a single repository, FastAPI's hosting, and JSON files for static data.

### Production Deployment Strategy

There are several steps that I would take before deploying this as a true production app.

- **Performance & Availability**  
  Move scoring and data storage to background jobs/workers. Manage workers via a load balancer (such as AWS Elastic Beanstalk). Serve the frontend separately from the backend.

- **Security**  
  Enforce HTTPS, configure strict CORS rules, validate all inputs, and restrict access to authenticated users. Add API rate limiting and audit logging. Since this is patient data, we might need to develop and follow specific SoPs due to HIPAA.

- **Monitoring & Debugging**  
  Add structured logging (console and persistent), health checks, CI/CD, and uptime monitoring. Integrate client-side error tracking.

### Trade-Offs & Future Improvements

I made quite a few decisions to guarantee that I can deliver the project within a tight timeframe. Prominent examples include:

- Domain map and screener are read from static JSON files instead of a database.
- Frontend is JS, not TypeScript (especially relevant for incoming data).
- Skipped client-side validation and user authentication.
- There are no backend tests.

Given more time, I would start by splitting the deployment and hosting the frontend separately from the backend.

Next, I would add strict typing to the frontend for safer API integration and introduce unit tests for the backend and potentially the frontend. I would move the scoring logic to a dedicated service layer, which would ideally be more dynamic (relying on a database instead of hard-coding strings and rules). Lastly, I would add error handling via logging, retry logic, and user-friendly errors on the frontend.

### LinkedIn

[https://www.linkedin.com/in/elli-el-ad-david-amir-68624b6/](https://www.linkedin.com/in/elli-el-ad-david-amir-68624b6/)

Thank you for your time and consideration!

