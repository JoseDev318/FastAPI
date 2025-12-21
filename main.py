from typing import Union
from fastapi import FastAPI

#Creacion de una Aplicacion FastAPI:
aplicacion = FastAPI()

@aplicacion.get("/")
def read_root():
    return {"Hello": "World"}

@aplicacion.get("/hola")
def hola_mundo():
    return{"Hablame": "Cachon"}

@aplicacion.get("/items/{item_id}")
def read_item(item_id:int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@aplicacion.get("/calculator")
def calcular(operando_1:float, operando_2:float):
    return {"suma": operando_1 + operando_2}