import time
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.ports.api.v1 import api_v1

app = FastAPI(debug=True)  # pylint: disable=invalid-name

base_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=str(base_dir / "static")),
          name="static")
app.mount("/api/v1", api_v1)

templates = Jinja2Templates(directory=str(base_dir / "templates"))


@app.get("/health")
def health_check():
    return {}


@app.get("/.*")
async def index(request: Request):
    """Index url, let frontend handle all routes."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.middleware("http")
async def add_service_worker_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['Service-Worker-Allowed'] = '/'
    response.headers["X-Process-Time"] = str(process_time)

    return response

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8443)
