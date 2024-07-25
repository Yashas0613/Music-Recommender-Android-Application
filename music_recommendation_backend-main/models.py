from dataclasses import dataclass

from pydantic import BaseModel


class RecommendationScheme(BaseModel):
    artist_name: str
    genres: list[str]
    attrs: dict


@dataclass
class Music:
    name: str
    link: str
    artist: str
    image_link: str
