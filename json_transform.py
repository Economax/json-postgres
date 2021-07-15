import json
from jsonschema import validate
from json_config import incoming_schema as incoming_schema
from json_config import outgoing_schema
from datetime import datetime, timezone
import traceback

###This class defines the extraction and transformation logic

class JsonTransformer:
    
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    
    
    def __init__(self):
        
        #This is a correspondence from json key value to the transformations those keys are associated with
        self.conversions = {"address":self.map_address, "author":self.map_author, "id":self.map_id,
                    "created":self.map_created, "counters":self.map_counters,
                    "content":self.map_content, "updated":self.map_updated}
        
        self.soft_errors = False
        self.silent = False
        self.bcolors = self.bcolors()
    
    
    
    def set_soft_errors(self, flag):
        self.soft_errors = flag
    
    
    
    def set_silent(self, flag):
        self.silent = flag
    
    
    
    def eprint(self, text):
        if not self.silent:
            print(self.bcolors.WARNING + text + self.bcolors.ENDC)
        
        

    #In place modification
    def map_address(self, json_info, convert):
        inkey = "address"
        outkey = "path"
        #due to passing validation, we know that address contains a string
        #futher input testing can be implemented here if necessary
        convert[outkey] = json_info[inkey]



    def map_author(self, json_info, convert):
        inkey_l1 = "author"
        inkey_l2_1 = "username"
        inkey_l2_2 = "id"
        outkey_1 = "author_name"
        outkey_2 = "author_id"
        #we know that both username and id exist and are strings due to validation
        convert[outkey_1] = json_info[inkey_l1][inkey_l2_1]
        convert[outkey_2] = json_info[inkey_l1][inkey_l2_2]



    def map_id(self, json_info, convert):
        inkey = "id"
        outkey = "id"
        
        convert[outkey] = json_info[inkey]
        
        

    def map_created(self, json_info, convert):
        inkey = "created"
        outkey_1 = "created_date"
        outkey_2 = "created_time"

        #Some transformation
        cdata = json_info[inkey]
        
        #Precautionary copying
        convert[outkey_1] = cdata
        convert[outkey_2] = cdata
        
        correct_format = None
        
        try:
            correct_format = datetime.strptime(cdata, "%Y-%m-%dT%H:%M:%S%z")
            convert[outkey_1] = correct_format.strftime("%Y-%m-%d")
            convert[outkey_2] = correct_format.strftime("%H:%M:%S%z")
        except ValueError as e:
            if self.soft_errors:
                self.eprint("Json object with id {} has an inconsistent date time format in the 'created' property.".format(json_info["id"]))
                self.eprint("Handling error softly by copying original time data to new fields.")
            else:
                print(traceback.format_exc())
                raise Exception("Json object with id {} has an inconsistent date time format in the 'created' property.".format(json_info["id"]))
    
    
    
    def map_counters(self, json_info, convert):
        inkey_l1 = "counters"
        inkey_l2_1 = "A"
        inkey_l2_2 = "B"
        outkey = "counters_total"
        #Some data transformation
        
        convert[outkey] = json_info[inkey_l1][inkey_l2_1] + json_info[inkey_l1][inkey_l2_2]
        
        
        
    def map_updated(self, json_info, convert):
        inkey = "updated"
        outkey_1 = "updated_date"
        outkey_2 = "updated_time"

        #Some transformation
        cdata = json_info[inkey]
        
        #Precautionary copying
        convert[outkey_1] = cdata
        convert[outkey_2] = cdata
        
        correct_format = None
        
        try:
            correct_format = datetime.strptime(cdata, "%Y-%m-%dT%H:%M:%S%z")
            convert[outkey_1] = correct_format.strftime("%Y-%m-%d")
            convert[outkey_2] = correct_format.strftime("%H:%M:%S%z")
        except ValueError:
            if self.soft_errors:
                self.eprint("Json object with id {} has an inconsistent date time format in the 'updated' property.".format(json_info["id"]))
                self.eprint("Handling error softly by copying original time data to new fields.")
            else:
                print(traceback.format_exc())
                raise Exception("Json object with id {} has an inconsistent date time format in the 'updated' property.".format(json_info["id"]))
            
    
    
    def map_content(self, json_info, convert):
        #Here we need to do some testing, since fields are not required by schemas
        
        inkey_l1 = "content"
        inkey_l2_1 = "seasons"
        inkey_l2_2 = "description"
        
        if inkey_l2_1 in json_info[inkey_l1]:
            self.map_seasons(json_info, convert)
        if inkey_l2_2 in json_info[inkey_l1]:
            self.map_desc(json_info, convert)
        
        

    def map_seasons(self, json_info, convert):
        inkey_l1 = "content"
        inkey_l2_1 = "seasons"
        inkey_l3 = "text"
        outkey_1 = "seasons"
        
        #We don't need to do any type testing or structure testing, because json schema handles it
        #We might still want to set conditions on the content of the strings we extract
        
        sealist = []
        jsonsea = json_info[inkey_l1][inkey_l2_1]
        
        for element in jsonsea:
            if inkey_l3 in element: #This test is necessary because json schema doesn't require "text" to be only key
                sealist.append(element[inkey_l3])
                
        convert[outkey_1] = sealist
        
        

    def map_desc(self, json_info, convert):
        inkey_l1 = "content"
        inkey_l2_2 = "description"
        outkey_1 = "body"
        
        convert[outkey_1] = json_info[inkey_l1][inkey_l2_2]
        
        
        
    def transform_json(self, json_data):
        
        #Validate throws an exception if the schema cannot be validated
        try:
            validate(instance=json_data, schema=incoming_schema)
        except:
            print(traceback.format_exc())
            raise Exception("The incoming JSON object has not been formatted according to the specified JSON schema")
            
                
        conv_data = {}

        for key in json_data:
            if key in self.conversions:
                self.conversions[key](json_data, conv_data)


        #Throws an error if the data output does not conform to the json schema specification
        try:
            validate(instance=conv_data, schema=outgoing_schema)
        except:
            print(traceback.format_exc())
            raise Exception("An unknown transformation error has occured." + "\n" +
                "The outgoing JSON object has not been formatted according to the specified JSON schema.")
        
        return conv_data


