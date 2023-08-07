from aiokafka import AIOKafkaProducer


async def send_message(script_name, parameters, collection):
    bootstrap_servers = 'kafka:29092'
    topic = 'test_topic'
    producer = AIOKafkaProducer(bootstrap_servers=bootstrap_servers)
    await producer.start()
    try:
        message = f"{script_name},{parameters},{collection}"
        await producer.send_and_wait(topic, value=message.encode('utf-8'))
    finally:
        await producer.stop()
