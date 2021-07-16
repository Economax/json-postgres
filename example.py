from crud import PgAccessPoint
from json_transform import JsonTransformer
import json


# db_config.py sets database parameters for the postgres db which is used by crud.py, modify it to write to a different database
# models.py sets the data model for the table crud tries to generate or access
# crud.py defines an object that provides write and read (first) from the postgres db, it performs no checks and writes naively to a JSONB field
# json_config.py contains a filter (json schema) for json input and output, used by json_transform.py for two separate validations: 
# (1) The data passed to the transformer (2) The data returned by the transformer
# json_transform.py contains the extraction and transformation logic behind the json conversion
# the transformation process is entirely separate from the database access, and thus the two modules can be used and tested separately


json_list = []

###This json reader expects a newline separated file containing json objects
###You can find an example of the expected input data in the file "input_data.txt"
json_data_path = "input_data.txt"


#Reads json objects from a file containing json objects separated by newlines
with open(json_data_path, "r") as data:
    for line in data:
        json_list.append(json.loads(line))
        

#Instantiate transformer object and postgres access point
transformer = JsonTransformer()

#Modify the db_config.py file to write to a different database
#The constructor expects a boolean value telling it whether or not to try to create a new table in the database based on the model specified in models.py
ap = PgAccessPoint(True)

for json_obj in json_list:
    #transform_json receives any json object that conforms to the incoming schema defined in json_config
    new_json = transformer.transform_json(json_obj)
    #write_json accepts any json objects, all testing and conformance is done in the transformer
    ap.write_json(new_json)