from sqlalchemy import create_engine
from config import DATABASE_URI
#from sqlalchemy.ext.declarative import declarative_base
import time
from models import Base, JsonObject
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import json


class pgAccessPoint():
    def __init__(self) -> None:
        self.engine = create_engine(DATABASE_URI)
        
        #Create a new table based on the metadata collected by Base - this can safely be switched off if the table has been created
        Base.metadata.create_all(self.engine)
        
        self.Session = sessionmaker(bind=self.engine)
        self.UNIQUENESS = 10e2
    
    #Simply pass a python dictionary or json data
    def write_json(self, json_data):
        
        json_obj = JsonObject(
            id=int(float(str(time.time())[5:])*self.UNIQUENESS),
            data=json_data
        )
        
        with self.session_scope(self.Session) as s:
            s.add(json_obj)
            
    
    def read_json(self):
        with self.session_scope(self.Session) as s:
            q = s.query(JsonObject).first()
            json_data = q.data
            json_id = q.id
            
        return json_data
            
    
    @contextmanager
    def session_scope(self, Session):
        session = Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
            
            
pgdb = pgAccessPoint()
