from typing import Annotated, List, Dict

from fastapi import APIRouter, Depends
from ..dto.pizzas import SPizzasParam, SPizzaID, RPizza, RPizzasResponse
from sqlalchemy.orm import Session

router = APIRouter(tags=["Pizzas"])


@router.get("/", response_model=RPizzasResponse)
async def get_pizzas(data: Annotated[SPizzasParam, Depends()] = None):
    # print(data)
    return {
        "status": 200,
        "data": [
            RPizza(
                id=0,
                imageUrl="https://i.ibb.co/hZ09T29/photo-2024-05-09-22-10-03.jpg",
                title="Пепперони Фреш с перцем",
                types=[0, 1],
                sizes=[26, 30, 40],
                price=803,
                category=0,
                rating=4
            ),
            RPizza(
                id=0,
                imageUrl="https://i.ibb.co/hZ09T29/photo-2024-05-09-22-10-03.jpg",
                title="Пепперони Фреш с перцем",
                types=[0, 1],
                sizes=[26, 30, 40],
                price=803,
                category=0,
                rating=4
            )
        ]
    }
