from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

# creates an object/instance of FastAPI()
app = FastAPI()

# list of allowed origins to connect to our FastAPI application
origins = ["http://localhost:5173"]

# handles CORS policy
app.add_middleware(CORSMiddleware, allow_origins=origins)


# creates pydantic model that validates the requests from our react application
# and accepts or rejects the request based on the validation
class TransactionBase(BaseModel):
    amount: float
    category: str
    description: str
    is_income: bool
    date: str


class TransactionModel(TransactionBase):
    id: int

    class Config:
        orm_mode = True


# creates database and it makes sure that our database connection only opens
# when request comes in and always closes after the request is completed
def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # always close the database connection when done


# creates dependency injection for our application
db_dependency = Annotated[Session, Depends(get_database)]

# creates database and its tables, columns automatically when this FastAPI application is created
models.Base.metadata.create_all(bind=engine)


# API endpoints of our application


# post API to store the transaction details on database
@app.post("/transactions/", response_model=TransactionModel)
async def create_transaction(transaction: TransactionBase, db: db_dependency):
    db_transaction = models.Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


# get API request to retreive all the transaction data
@app.get("/transactions/", response_model=List[TransactionModel])
async def read_transactions(db: db_dependency, skip: int = 0, limit: int = 100):
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions
