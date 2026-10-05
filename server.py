"""Optional local server for SkillBridge AI: serves the website and the AI API.
Run: uvicorn server:app --host 127.0.0.1 --port 8000  (demo only; no login or production security).
Do not put API keys in HTML. Configure BEDROCK_MODEL_ID + AWS credentials, or OPENAI_API_KEY, on this server."""
from pathlib import Path
from fastapi import Body, FastAPI, HTTPException
from fastapi.responses import FileResponse, Response
import ai_core

app = FastAPI(title='SkillBridge AI | live AI backend')
ROOT = Path(__file__).parent


def _call(fn, body):
    try:
        return fn(body if isinstance(body, dict) else {})
    except ai_core.AIError as e:
        raise HTTPException(e.status, e.message)


@app.get('/')
def index():
    return FileResponse(ROOT / 'index.html')


@app.get('/config.js')
def config():
    path = ROOT / 'config.js'
    return FileResponse(path) if path.exists() else Response('window.SKILLBRIDGE_CONFIG={};', media_type='text/javascript')


@app.get('/api/status')
def status():
    return ai_core.status()


@app.post('/api/ai/coach')
def coach(body: dict = Body(...)):
    return _call(ai_core.coach, body)


@app.post('/api/ai/practice')
def practice(body: dict = Body(...)):
    return _call(ai_core.practice, body)


@app.post('/api/ai/cv')
def cv(body: dict = Body(...)):
    return _call(ai_core.cv_review, body)


@app.post('/api/ai/roadmap')
def roadmap(body: dict = Body(...)):
    return _call(ai_core.roadmap, body)
