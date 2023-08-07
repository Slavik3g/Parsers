from typing import List

from pydantic import BaseModel, HttpUrl


class StreamerDTO(BaseModel):
    id: str
    user_id: str
    user_login: str
    user_name: str
    game_id: str
    game_name: str
    type: str
    title: str
    viewer_count: int
    started_at: str
    language: str
    thumbnail_url: str
    tag_ids: List[str]
    tags: List[str]
    is_mature: bool


class GameDTO(BaseModel):
    id: str
    name: str
    box_art_url: HttpUrl
    igdb_id: str
