from __future__ import annotations
from typing import TypedDict, TYPE_CHECKING, cast

if TYPE_CHECKING:
    from typing import Optional
    from fastapi import Request


__all__ = (
    "ContextBuild",
)

class ContextData(TypedDict):
    request: Request
    site_title: str
    site_description: str
    site_image: str

class ContextBuild():
    def __init__(
        self, 
        request: Request,
        title: str, 
        description: str, 
        image_url: Optional[str] = None, 
    ) -> None:
        self.data = cast(
            ContextData, {
                "request": request, 
                "site_title": title, 
                "site_description": description, 
                "site_image": image_url
            }
        )