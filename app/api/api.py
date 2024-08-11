from typing import List

from fastapi import APIRouter       
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from .. import utils
from ..osaka import OsakaData
from . import errors

__all__ = ("api",)

api = APIRouter()

@api.get(
    "/api/search",
    response_class = JSONResponse,
    responses = {
        200: {
            "description": "Returns JSON Metadata for query",
        },
    }
)
async def search(request: Request, query: str):
    return utils.search(query, request.app.azumanga.osakas)

@api.get(
    "/api/get/{id}",
    response_class = JSONResponse,
    responses = {
        200: {
            "model": OsakaData,
            "description": "Returned an JSON Metadata for given ID",
        },
        404: {
            "model": errors.NotFound,
            "description": "Failed to find ID"
        },
    }
)
async def get(request: Request, id: str):
    result = request.app.azumanga.get(id)

    if result is not None:
        return result.to_dict()

    return JSONResponse(
        status_code = 404, 
        content = {
            "error": "NotFound",
            "message": f"We could not find anything with the search id '{id}'!"
        }
    )

@api.get(
    "/api/random",
    response_class = JSONResponse,
    responses = {
        200: {
            "model": OsakaData,
            "description": "Returns a random Osaka.",
        }
    }
)
async def api_random(request: Request, category: str = None):
    return request.app.azumanga.get_random(category).to_dict()

@api.get(
    "/api/category/{id}",
    response_class = JSONResponse,
    responses = {
        200: {
            "model": List[OsakaData],
            "description": "Returned an JSON Metadata for given category",
        },
        404: {
            "model": errors.CategoryNotFound,
            "description": "Failed to find category"
        },
    }
)
async def category_get(request: Request, id: str):
    results = request.app.azumanga.categories.get(id)

    if results is not None:
        return [
            result.to_dict() for result in results
        ]

    return JSONResponse(
        status_code = 404, 
        content = {
            "error": "CategoryNotFound",
            "message": f"The category '{id}' was not found!"
        }
    )

@api.get(
    "/api/categories",
    response_class = JSONResponse,
    responses = {
        200: {
            "model": List[str],
            "description": "Returned an all avaliable categories",
        }
    }
)
async def categories(request: Request):
    return list(request.app.azumanga.categories.keys())