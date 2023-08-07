import asyncio

from aiokafka import AIOKafkaConsumer

from src.config.database import Database
from src.controller.lamoba_controller import LamodaController
from src.controller.twitch_controller import TwitchController
from src.parsers.lamoda_parser import get_products
from src.parsers.twitch_parser import get_data_from_api


async def process_message(message: str):
    script_name, url, collection = message.split(',')
    if script_name == "lamoda_parser":
        database = Database(collection)
        lamoda_controller = LamodaController(database)
        lamoda_controller.create_positions(await get_products(url))
    elif script_name == "twitch_parser":
        database = Database(collection)
        twitch_controller = TwitchController(database)
        twitch_controller.create_positions(await get_data_from_api(url))
    else:
        print("Unknown script name:", script_name)


async def read_messages():
    bootstrap_servers = 'kafka:29092'
    topic = 'test_topic'
    loop = asyncio.get_event_loop()
    consumer = AIOKafkaConsumer(topic, bootstrap_servers=bootstrap_servers, loop=loop)
    await consumer.start()
    try:
        async for message in consumer:
            await process_message(message.value.decode('utf-8'))
    finally:
        await consumer.stop()
