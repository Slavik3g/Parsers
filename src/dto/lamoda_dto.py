from pydantic import BaseModel


class ProductDto(BaseModel):
    brand: str
    description: str
    price: str


class ProductDBDto(BaseModel):
    brand: str
    description: str
    price: str
    created_at: str
