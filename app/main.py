from fastapi import FastAPI
from fastapi.responses import StreamingResponse    
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .ctx import ContextBuild
from .utils import search, stream
from . import  __version__

from .api import api
from .azumanga import Azumanga
import httpx

azumanga = Azumanga()

app = FastAPI(
    title = "sata-andagi.moe API", 
    license_info = {
        "name": "GPL-3.0",
    }, 
    swagger_favicon_url = "https://avatars.githubusercontent.com/u/172095443?s=200", 
    version = f"v{__version__}",
)

app.azumanga = azumanga

app.include_router(api)

templates = Jinja2Templates(directory = "./templates")

@app.get("/")
async def home(request: Request, q: str = None):
    if q is not None:
        osakas = search(q.replace("%20", " "), azumanga.osakas)
    else:
        osakas = azumanga.osakas
    
    if "Discordbot" in request.headers.get("User-Agent"):
        return StreamingResponse(stream(azumanga.get_random().url), media_type='application/octet-stream')
     
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