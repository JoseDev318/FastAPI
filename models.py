from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    name:str 
    descripcion: str | None
    email:str
    age: int

class Transaction(BaseModel):
    id: int
    ammount: int
    descripcion: str

class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def ammount_total(self):
        return sum(transaction.ammount for transaction in self.transactions)
