import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    
    ]
}
'''
#For now, this is just a string to python that happens to be a valid json object.

#How do we turn this string into a python object?

#We can use a json method called loads to transform the python string into a python object.

data = json.loads(people_string)

#print(type(data))
#print(type(data["people"]))

#How to access each one of those people individually ?

for person in data["people"]:
    #Access each person details
    #print(person)

    #Access each person name
    #print(person["name"])

# HOW CAN WE MODIFY A JSON FILE ? FPR EXAMPLE, LET'S DELETE THEIR PHONE NUMBERS.
    #
    del person["phone"]
#We dump the new data into the variable, we some indententions to make it readable
new_string = json.dumps(data, indent=3)

print(new_string)