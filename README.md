# SkillBridge AI

**UJ × Vodacom × AWS Hackathon 2026 — Skills-to-Work Bridge prototype**

SkillBridge AI is a hackathon prototype exploring how a job seeker could understand opportunity requirements, demonstrate selected skills, review a CV, identify development gaps and use an AI career coach from one interface.

> **Demo boundary:** all candidate profiles and opportunities in this repository are synthetic. SkillProof badges are internal hackathon demonstrations, not formal credentials. No real job application is sent.

![SkillBridge AI preview](docs/skillbridge-preview.svg)

## Live prototype

https://main.dgjytvhyaiz2d.amplifyapp.com

## What the prototype demonstrates

- Synthetic opportunity matching with mandatory requirements separated from preferred skills.
- Internal **SkillProof** assessments for selected skills.
- A browser-based **CV & ATS check** with a transparent rule-based score.
- Optional AI CV feedback through a server-side model integration.
- A personalised **growth roadmap** based on profile, gaps and CV findings.
- An **AI Career Coach** area designed around Amazon Quick, with an honest fallback when embedding is unavailable.
- A coordinator/recommendation flow implemented as a same-device simulation for the hackathon demo.

## Tech stack

- **Frontend:** HTML, CSS and JavaScript
- **Backend option:** Python + FastAPI
- **AWS hosting:** AWS Amplify
- **Serverless option:** AWS Lambda
- **AI option:** Amazon Bedrock
- **Career coach:** Amazon Quick embed / link configuration

## Repository structure

```text
.
├── index.html
├── config.js
├── ai_core.py
├── server.py
├── requirements.txt
├── SkillBridge_Quick_Demo_Knowledge.txt
├── aws_lambda/
│   ├── ai_core.py
│   ├── lambda_function.py
│   └── iam-policy.json
└── docs/
    └── skillbridge-preview.svg
```

## Run locally

```bash
pip install -r requirements.txt
uvicorn server:app --port 8000
```

Then open `http://127.0.0.1:8000`.

For AI features, configure a supported server-side provider as described below. Do not put API keys or passwords in `config.js`.

## AWS deployment outline

### Static website

1. Deploy `index.html` and `config.js` through AWS Amplify Hosting.
2. Use the Amplify URL as the allowed domain for the Amazon Quick embed if that feature is enabled.

### AI API

1. Create a Python 3.12 Lambda function.
2. Deploy the `aws_lambda/` code.
3. Configure the Bedrock model ID server-side.
4. Give the function only the Bedrock permissions it needs.
5. Put the public Function URL in `config.js` as `AI_API_BASE`.

## Important limitations

- Amazon Quick does not automatically receive profile, exam or CV data; the demo prepares context for the user to copy.
- Embedded chat may require Quick sign-in and domain allow-listing.
- The ATS score is a transparent rule-based estimate, not a real employer ATS decision.
- AI CV feedback is advice only.
- A public Lambda Function URL without authentication/rate limiting is suitable only for a short-lived demo.
- The coordinator view is simulated on the same device; there is no production account system.

## Why this project matters

The project focuses on the gap between *having skills* and *being able to understand, demonstrate and communicate those skills for an opportunity*. It brings opportunity matching, evidence, CV feedback and a learning path into one hackathon prototype while clearly separating real integrations from simulated behaviour.
