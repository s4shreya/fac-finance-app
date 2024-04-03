# creates tables in our SQLite database

from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

# creates a class that inherits from the Base class
class Transaction(Base):
    __tablename__ = "transactions"  # SQLAlchemy will create a table named transactions in the SQLite database

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    is_income = Column(Boolean)
    date = Column(String)