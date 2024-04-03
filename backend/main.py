from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

# creates an object/instance of FastAPI()
app = FastAPI()

# list of allowed origins to connect to our FastAPI application
origins = ["http://localhost:3000"]

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
