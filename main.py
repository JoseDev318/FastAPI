import zoneinfo
from datetime import datetime

from typing import Union
from fastapi import FastAPI
from models import Customer, Transaction, Invoice


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


country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@aplicacion.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}

@aplicacion.post("/costumers")
async def create_customer(customer_data: Customer):
    return customer_data

@aplicacion.post("/transactions")
async def create_transaction(transaction_data: Transaction):
    return transaction_data

@aplicacion.post("/invoices")
async def create_invoice(invoice_data: Invoice):
    return invoice_data

    
    