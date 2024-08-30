import uvicorn
from fastapi import FastAPI
from src.routers.pizzas import router as PizzasRouter

app = FastAPI(title="ReactPizza API", version="0.0.1")

app.include_router(PizzasRouter, prefix="/api/v1/items")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3001, reload=True, workers=3)
