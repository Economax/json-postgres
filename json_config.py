### This class defines the schemas for incoming and outgoing json objects
### Validates data types and most data structures - not all can be validated while allowing flexibility in inputs
### Schemas can also validate the input values received, but since tolerances have not been defined, this has not been implemented

incoming_schema = {
    "type" : "object",
    "properties" : {
        "address" : {"type" : "string"},
        "content" : {"type" : "object",
                    "properties" : {
                        "seasons":{"type" : "array",
                                    "items" : {"type" : "object",
                                                "properties" : {
                                                    "text" : {"type":"string",}
                                                }
                                    }                        
                        }, 
                        "description":{"type" : "string"}
                    }
        },
        "updated" : {"type" : "string"},
        "author" : {"type" : "object",
                    "properties" : {
                        "username" : {"type" : "string"},
                        "id" : {"type" : "string"}
                    },
                    "required" : ["username", "id"]
        },
        "id" : {"type" : "string"},
        "created" : {"type" : "string"},
        "counters" : {"type" : "object",
                        "properties" : {
                            "A" : {"type" : "integer"},
                            "B" : {"type" : "integer"}
                        },
                        "required" : ["A", "B"]
                    },
        "type" : {"type" : "string"},
    },
    "required": ["address", "author", "id", "created", "counters"]
}


outgoing_schema = {
    "type" : "object",
    "properties" : {
        "path" : {"type" : "string"},
        "seasons":{"type" : "array",
                    "items" : {"type" : "string"}                        
        }, 
        "body":{"type" : "string"},
        "updated_date" : {"type" : "string"},
        "updated_time" : {"type" : "string"},
        "author_username" : {"type" : "string"},
        "author_id" : {"type" : "string"},
        "id" : {"type" : "string"},
        "created_date" : {"type" : "string"},
        "created_time" : {"type" : "string"},
        "counters_total" : {"type" : "integer"},
        "type" : {"type" : "string"},
    },
    "required": ["path", "author_name", "author_id", "id", "created_date", "created_time", "counters_total"]
}
