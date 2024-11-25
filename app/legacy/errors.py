from pydantic import BaseModel

__all__ = (
    "CategoryNotFound",
    "NotFound",
)
    
class CategoryNotFound(BaseModel):
    error: str
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "error": "CategoryNotFound",
                    "message": "The category 'osaka' was not found!"
                }
            ]
        }
    }

class NotFound(BaseModel):
    error: str
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "error": "NotFound",
                    "message": "We could not find anything with the search id 'ohmygah'!"
                }
            ]
        }
    }