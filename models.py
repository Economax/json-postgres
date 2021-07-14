from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from config import table_name

Base = declarative_base()



class JsonObject(Base):
    
    #This variable is set in the config.py file
    __tablename__ = table_name
    
    id = Column(Integer, primary_key=True)
    
    data = Column(JSONB)
    
    