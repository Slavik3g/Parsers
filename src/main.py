from fastapi import FastAPI
import asyncio
from src.consumer.consumer import read_messages
from src.routers.lamoda_routers import router as lamoda_router
from src.routers.twitch_routers import router as twitch_router

app = FastAPI()

app.include_router(lamoda_router)
app.include_router(twitch_router)

asyncio.create_task(read_messages())
