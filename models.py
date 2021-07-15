from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from db_config import table_name

### This class defines the data model used in the Postgres DB table we write json objects to
### Note that we are assuming that JSONB is a valid column type

Base = declarative_base()

class JsonObject(Base):
    
    #This variable is set in the config.py file
    __tablename__ = table_name
    
    id = Column(Integer, primary_key=True)
    
    data = Column(JSONB)
    
    