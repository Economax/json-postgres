from crud import PgAccessPoint
from json_transform import JsonTransformer
import json


json_data = []

with open("input_data.txt", "r") as data:
    for line in data:
        json_data.append(json.loads(line))
        
        
transformer = JsonTransformer()
ap = PgAccessPoint(False)

for json_obj in json_data:
    new_json = transformer.transform_json(json_obj)
    print(new_json)
    ap.write_json(new_json)