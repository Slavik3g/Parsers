import asyncio

import aiohttp
from bs4 import BeautifulSoup

from src.config.database import Database
from src.controller.lamoba_controller import LamodaController


async def get_products(link):
    async with aiohttp.ClientSession() as session:
        products_list = []
        page_num = 1
        while True:
            async with session.get(f"{link}?page={page_num}") as response:
                response_text = await response.text()
            soup = BeautifulSoup(response_text, "html.parser")
            all_clothes = soup.findAll('div', class_='x-product-card__card')
            if not all_clothes:
                return products_list
            for cloth in all_clothes:
                data = dict()
                data['price'] = cloth.find('span',
                                           class_='x-product-card-description__price-WEB8507_price_no_bold').text
                data['brand'] = cloth.find('div', class_='x-product-card-description__brand-name').text
                data['product'] = cloth.find('div', class_='x-product-card-description__product-name').text
                products_list.append(data)
            page_num += 1


def data():
    database = Database()
    lamoda_controller = LamodaController(database.db)
    lamoda_controller.create_positions(asyncio.run(get_products("https://www.lamoda.by/c/4418/clothes-body/")))
