from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[UUID] = uuid4
    first_name: str
    last_name: str