from crud import PgAccessPoint
from json_transform import JsonTransformer
import json


json_list = []

###The json reader expects a newline separated file containing json objects
json_data_path = "input_data.txt"


#Reads json objects from a file containing json objects separated by newlines
with open(json_data_path, "r") as data:
    for line in data:
        json_list.append(json.loads(line))
        

#Instantiate transformer object and postgres access point
transformer = JsonTransformer()

#Modify the db_config.py file to write to a new database
#The constructor expects a boolean value telling in whether or not to try to create a new table based on the model specified in models.py
ap = PgAccessPoint(True)

for json_obj in json_list:
    #transform_json receives any json object that conforms to the incoming schema defined in json_config
    new_json = transformer.transform_json(json_obj)
    #write_json accepts any json objects, all testing and conformance is done in the transformer
    ap.write_json(new_json)