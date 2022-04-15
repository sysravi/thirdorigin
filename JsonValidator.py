"""
Validate a Json against a given schema file

Create a class called JsonValidator .The class should be able to validate 
	1. required fields. Example id, name field to be declared as they are mandatory
	2. atleast one of many fields to be present. Example one of home phone or cell phone or work phone fields
	3. either one field or another field  Either birth date or govt id number
	4. mutually exclusive fields (if one is present, the other should not be present)
	5. field value to be one of a set of values. Example field day can have only one of SU,MO,TU,WE,TH,FR,SA (enum)


	Define the following methods
	1. validate_schema(json_file, schema_file, schema_integrity_file)
	   method should return True or False if validation succeeds or fails

"""


import json
import jsonschema
from jsonschema import validate

def get_schema():
    """This function loads the given schema available"""
    with open('json_file.json', 'r') as file:
        f = json.load(file)
    return f

def get_integ():
    with open('schema_integrity_file.json', 'r') as file:
        f = json.load(file)
    return f

class JsonValidator:
    def __init__(self) -> None:
        pass

    def validate_schema(json_file,schema_file,schema_integrity_file):
        try:
            validate(instance=json_file, schema=schema_file)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            err = "Given JSON data is Invalid"
            
            return False, err

        print("Given JSON data is Valid")
        return True

schema = get_schema()
integ = get_integ()

jv = JsonValidator()
jv.validate_schema(schema,schema)
