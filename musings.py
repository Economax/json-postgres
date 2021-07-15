"""
#If incoming type is object or array: iterate
 
#If outgoing type is object, create dictionary
#If outgoing type is array, create list

#If type is integer or string, try to cast data and transfer - raise error if casting is impossible



#If the mapping results in a dictionary, do recursion:

mapping = {"author":["test", {"id":"author_id", "username":"author_username"}]}

def dictcurse(datadict):
    
    for key in datadict:
        if datadict[key]["type"] == "object":
            pass #Dictionary iteration

def recurse(recu_obj):
    
    
    
    if (type(recu_obj) is dict):
        for obj in recu_obj:
            value = recurse(recu_obj[obj])
            print("{}, {}".format(obj, value))
            
            #Actions happens here: Make decisions on data transfer
            #First, we need to make sure that we have a value that maps into outgoing_schema
            
            
    elif (type(recu_obj) is list):
        for obj in recu_obj:
            value = recurse(obj)
            print("{}, {}".format(obj, value))
            
            #Action happens here too: Decisions on data transfer
            
    else:
        #This returns none on author - why?
        return recu_obj
"""