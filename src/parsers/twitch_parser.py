import aiohttp

from src.config.twitch import TwitchDAO

tw = TwitchDAO(
    {
        "Authorization": "Bearer ngrdpixm4eb21ggdkw2nhluibo36co",
        "Client-Id": "7j4j5m4g4mka15vth8nfdjokyoz89e"
    }
)


async def get_data_from_api(url):
    async with aiohttp.ClientSession(headers=tw.headers) as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                print(data['data'])
                return data.get("data", [])
            else:
                print(f"Error: Unable to fetch streams. Status Code: {response.status}")
                return []
