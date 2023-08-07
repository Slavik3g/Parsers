from fastapi import APIRouter, Request
from src.config.config import Config
from src.config.database import Database
from src.controller.lamoba_controller import LamodaController
from src.dto.lamoda_dto import ProductDto
from src.producer.producer import send_message

config = Config()

router = APIRouter(
    prefix='/lamoda'
)

database = Database("clothes")
lamoda_controller_instance = LamodaController(database)


@router.get("/get_product/{item_id}")
async def get_product(item_id: str):
    return lamoda_controller_instance.get_position(item_id)


@router.get("/get_all_products")
async def get_all_products():
    return lamoda_controller_instance.get_positions()


@router.put("/update_product/{item_id}")
async def update_product(item_id: str, request: Request):
    data = await request.json()
    instance = ProductDto(**data)
    return lamoda_controller_instance.update_position(item_id, instance.model_dump())


@router.delete("/delete_product/{item_id}")
async def delete_product(item_id: str):
    return lamoda_controller_instance.delete_position(item_id)


@router.post("/create_product")
async def create_product(request: Request):
    data = await request.json()
    instance = ProductDto(**data)
    return lamoda_controller_instance.create_position(instance.model_dump())


@router.post('/parse_lamoda/')
async def parse_lamoda(request: Request):
    url = await request.json()
    await send_message('lamoda_parser', url['url'])
    return {"message": "Parsing request sent to Kafka"}
