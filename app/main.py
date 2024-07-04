from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .ctx import ContextBuild

from .azumanga import Azumanga
from .utils import search

app = FastAPI()
templates = Jinja2Templates(directory = "./templates")
azumanga = Azumanga()

@app.get("/")
async def home(request: Request, q: str = None):
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
        "index.html", {
            **context.data,
            "osakas": osakas,
            "random_embed_url": azumanga.get_random().url
        }
    )

app.mount("/", StaticFiles(directory = "static"))           