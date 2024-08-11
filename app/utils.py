from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Tuple
    from .osaka import Osaka

from thefuzz import fuzz

__all__ = ("search",)

def search(query: str, osakas: List[Osaka]) -> List[Osaka]:
    osakers: List[Tuple[int, Osaka]] = []

    for osaka in osakas:
        name_match = fuzz.partial_ratio(osaka.title.lower(), query.lower())

        if name_match > 70:
            osakers.append((name_match, osaka))

    osakers.sort(key = lambda x: x[0], reverse = True) # Sort in order of highest match.

    return [
        osaker[1].to_dict() for osaker in osakers
    ]