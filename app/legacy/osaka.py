from dataclasses import dataclass, field
from typing_extensions import TypedDict, final

__all__ = ("Osaka", "OsakaData")

@final
class OsakaData(TypedDict):
    id: str
    title: str
    url: str
    category: str
    source: str

@dataclass
class Osaka:
    id: str = field(default=None)
    title: str = field(default=None)
    url: str = field(default=None)
    category: str = field(default=None)
    source: str = field(default=None)

    def to_dict(self) -> OsakaData:
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "category": self.category,
            "source": self.source
        }