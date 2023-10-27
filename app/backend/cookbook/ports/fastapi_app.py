import time
from pathlib import Path

from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from cookbook.ports.api.v1 import get_v1
from cookbook.ports.bindings_schema import Bindings


def create_app(bindings: Bindings) -> FastAPI:
    app = FastAPI(debug=True)  # pylint: disable=invalid-name

    base_dir = Path(__file__).parent
    app.mount("/static", StaticFiles(directory=str(base_dir / "static")),
              name="static")
    app.mount("/api/v1", get_v1(bindings))

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

    return app
