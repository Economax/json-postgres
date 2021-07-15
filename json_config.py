schema = {
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
                        }
                    },
        "type" : {"type" : "string"},
    },
    "required": ["address", "author", "id", "created", "counters"]
} 
#Changes aren't being tracked anymore