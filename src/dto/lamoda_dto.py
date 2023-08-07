from pydantic import BaseModel


class ProductDto(BaseModel):
    brand: str
    description: str
    price: str
