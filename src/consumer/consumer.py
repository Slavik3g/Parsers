import asyncio

from aiokafka import AIOKafkaConsumer

from src.config.database import Database
from src.controller.lamoba_controller import LamodaController
from src.parsers.lamoda_parser import get_products


async def process_message(message: str):
    script_name, url = message.split(',')
    if script_name == "lamoda_parser":
        database = Database("clothes")
        lamoda_controller = LamodaController(database)
        lamoda_controller.create_positions(await get_products(url))
    elif script_name == "twitch_parser":
        database = Database("steamers")
        # twitch_parser(parameters)
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
