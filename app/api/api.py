from fastapi import APIRouter       
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from .. import utils
from . import errors

__all__ = ("api", "set_azumanga")

api = APIRouter()

@api.get(
    "/api/search/{query}",
    response_class = JSONResponse,
    responses = {
        200: {
            "description": "Returns JSON Metadata for query",
        },
    }
)
async def search(request: Request, query: str):
    search_results = utils.search(query.replace("%20", "  "), request.app.azumanga.osakas)

    return [
        result.to_dict() for result in search_results
    ]
    
@api.get(
    "/api/get/{id}",
    response_class = JSONResponse,
    responses = {
        200: {
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
    "/api/category/{id}",
    response_class = JSONResponse,
    responses = {
        200: {
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
            "description": "Returned an JSON Metadata for given ID",
        },
    }
)
async def categories(request: Request):
    return list(request.app.azumanga.categories.keys())