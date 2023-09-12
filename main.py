#importing all the required modules
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, Session
from typing import List
from pydantic import BaseModel

# Creating the FastAPI app
app = FastAPI()

# To Create SQLite database and SQLAlchemy engine
DATABASE_URL = "sqlite:///./addresses.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Defining the SQLAlchemy model for addresses
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#creating class to hold attributes of the address
class Address(Base):
 __tablename__ = "addresses"
 id = Column(Integer, primary_key=True, index=True)
 name = Column(String, index=True)
 street = Column(String)
 city = Column(String)
 state = Column(String)
 zip_code = Column(String)
 latitude = Column(Float)
 longitude = Column(Float)


# Create the database tables
Base.metadata.create_all(bind=engine)


# Pydantic model for address input
class AddressCreate(BaseModel):
 name: str
 street: str
 city: str
 state: str
 zip_code: str
 latitude: float
 longitude: float


# Pydantic model for address retrieval
class AddressRetrieve(AddressCreate):
 id: int


# Create an address
@app.post("/addresses/", response_model=AddressRetrieve)
def create_address(address: AddressCreate, db: Session = Depends(SessionLocal)):
 db_address = Address(**address.dict())
 db.add(db_address)
 db.commit()
 db.refresh(db_address)
 return db_address


# Update an address
@app.put("/addresses/{address_id}/", response_model=AddressRetrieve)
def update_address(
 address_id: int, address: AddressCreate, db: Session = Depends(SessionLocal)
):
 db_address = db.query(Address).filter(Address.id == address_id).first()
 if db_address is None:
 raise HTTPException(status_code=404, detail="Address not found")
 for key, value in address.dict().items():
 setattr(db_address, key, value)
 db.commit()
 db.refresh(db_address)
 return db_address


# Delete an address
@app.delete("/addresses/{address_id}/", response_model=AddressRetrieve)
def delete_address(address_id: int, db: Session = Depends(SessionLocal)):
 db_address = db.query(Address).filter(Address.id == address_id).first()
 if db_address is None:
 raise HTTPException(status_code=404, detail="Address not found")
 db.delete(db_address)
 db.commit()
 return db_address


if __name__ == "__main__":
 import uvicorn

 uvicorn.run(app, host="127.0.0.1", port=8081)
