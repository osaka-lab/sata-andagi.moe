from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from .osaka import Osaka

from thefuzz import fuzz
import httpx

__all__ = ("search", "stream")

def search(query: str, osakas: List[Osaka]) -> List[Osaka]:
    return sorted(osakas, key=lambda x: fuzz.ratio(query, x.title), reverse=True)

async def stream(url):
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", url) as response:
            async for chunk in response.aiter_bytes():
                yield chunk