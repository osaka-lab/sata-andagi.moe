from typing import Optional

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi_tailwind import tailwind
from contextlib import asynccontextmanager

from .ctx import ContextBuild
from .config import Config
from . import  __version__

from .legacy import api
from .legacy.utils import search
from .legacy.azumanga import Azumanga

azumanga = Azumanga()

static_files = StaticFiles(directory = "static")

@asynccontextmanager
async def lifespan(_: FastAPI):
    process = tailwind.compile(
        static_files.directory + "/output.css",
        tailwind_stylesheet_path = "./static/input.css"
    )

    yield

    process.terminate()


app = FastAPI(
    title = "sata-andagi.moe", 
    license_info = {
        "name": "GPL-3.0",
    }, 
    lifespan=lifespan,
    swagger_favicon_url = "https://github.com/osaka-lab.png", 
    version = f"v{__version__}",
)

app.azumanga = azumanga

config = Config()

app.include_router(api)

templates = Jinja2Templates(directory = "./templates")

@app.get("/", include_in_schema = False)
async def home(request: Request):
    context = ContextBuild(
        request = request,
        title = "Osaka-Lab",
        description = "Everything around Azumanga Daioh"
    )

    return templates.TemplateResponse(
        "index.html", {
            **context.data,
            "projects": config.projects
        }
    )

@app.get("/members", include_in_schema = False)
async def members(request: Request):
    context = ContextBuild(
        request = request,
        title = "Osaka-Lab",
        description = "Members at Osaka-Lab"
    )

    return templates.TemplateResponse(
        "members.html", {
            **context.data,
            "members": config.members
        }
    )

@app.get("/memes", include_in_schema = False)
@app.get("/legacy", include_in_schema = False)
async def memes(request: Request, q: Optional[str] = None):
    if q is not None:
        osakas = search(q.replace("%20", " "), azumanga.osakas)
    else:
        osakas = azumanga.osakas

    context = ContextBuild(
        request = request,
        title = "Saataa Andagii",
        description = "Azumanga Daioh"
    )

    return templates.TemplateResponse(
        "memes.html", {
            **context.data,
            "osakers": osakas
        }
    )

app.mount("/", static_files)