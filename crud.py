from sqlalchemy import create_engine
from db_config import DATABASE_URI
import time
from models import Base, JsonObject
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import json

###This class defines the loading/writing to database logic
### You can manually set DATABASE_URI as a parameter if preferred, either here or in db_config.py

class PgAccessPoint:
    
    def __init__(self, create_model_table):
        self.engine = create_engine(DATABASE_URI)
        self.create_model_table = create_model_table
        
        #Create a new table based on the metadata collected by Base - this can safely be switched off if the table has been created
        if create_model_table:
            Base.metadata.create_all(self.engine)
        
        self.session_factory = sessionmaker(bind=self.engine)
        self.UNIQUENESS = 10e2
    
    #Simply pass a python dictionary or json data
    def write_json(self, json_data):
        
        json_obj = JsonObject(
            id=int(float(str(time.time())[4:])*self.UNIQUENESS),
            data=json_data
        )
        
        with self.session_scope() as s:
            s.add(json_obj)
            
    
    def read_first_json(self):
        with self.session_scope() as s:
            q = s.query(JsonObject).first()
            json_data = q.data
            json_id = q.id
            
        return json_id, json_data
            
    
    @contextmanager
    def session_scope(self):
        session = self.session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
            
            