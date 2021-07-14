from jsonschema import validate
from json_config import schema as valid_schema


json_data = {"address" : "https://www.google.com ",
    "content" : {"seasons" : [{"text": "winter"},{"text": "spring"},{"text":"summer"},{"text": "autumn"}],"description" : "All seasons"},
    "updated" : "2021-02-26T08:21:20+00:00",
    "author" : {"username" : "Bob","id" : "68712648721648271"},
    "id" : "543435435",
    "created" : "2021-02-25T16:25:21+00:00",
    "counters" : {"A" : 3,"B" : 0},
    "type" : "main"}




print(validate(instance=json_data, schema=valid_schema))