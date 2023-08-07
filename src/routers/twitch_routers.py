import asyncio
from typing import List

from fastapi import APIRouter

from src.config.database import Database
from src.controller.twitch_controller import TwitchController
from src.dto.twitch_dto import StreamerDTO, GameDTO
from src.producer.producer import send_message

router = APIRouter(
    prefix='/twitch'
)


@router.get('/parse_streamers')
async def parse_streamers():
    url = "https://api.twitch.tv/helix/streams/"
    await send_message("twitch_parser", url, "streamers")
    return {"message": "Parsing request sent to Kafka"}


@router.get('/parse_top_games')
async def parse_top_games():
    url = 'https://api.twitch.tv/helix/games/top'
    await send_message("twitch_parser", url, "top_games")
    return {"message": "Parsing request sent to Kafka"}


@router.get('/get_streamers/')
async def get_streamers() -> List[StreamerDTO]:
    database = Database('streamers')
    twitch_controller = TwitchController(database)
    return twitch_controller.get_positions()


@router.get('/get_top_games/')
async def get_top_games() -> List[GameDTO]:
    database = Database('top_games')
    twitch_controller = TwitchController(database)
    return twitch_controller.get_positions()

