from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base  
import os



# Use environment variable for the database URL if available, or default to this one
DATABASE_URL = "mysql+mysqlconnector://root:123@localhost:3307/crud-fastapi"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"connect_timeout": 10})

# Create a session factory bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create all database tables
def connect_db():
    try:
        # Creates all tables based on the models defined
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Error while connecting to the database: {e}")
        raise e  

# Function to disconnect from the database
def disconnect_db():

    try:
        pass
    except Exception as e:
        print(f"Error while disconnecting: {e}")
        raise e  

