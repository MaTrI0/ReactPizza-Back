from typing import List
from pydantic import BaseModel

class SPizzaID(BaseModel):
    id: int

class SPizzasParam(BaseModel):
    page: int = 1
    limit: int = 4
    category: int | None = None
    sortBy: str | None = None
    order: str | None = None

class RPizza(BaseModel):
    id: int
    imageUrl: str
    title: str
    types: list
    sizes: List[int]
    price: int
    category: int
    rating: int

class RPizzas(BaseModel):
    items: List[RPizza]


class RPizzasResponse(BaseModel):
    status: int
    data: RPizzas
