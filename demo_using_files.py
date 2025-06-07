import json

with open('states.json') as f:
    data = json.load(f)


for state in data["states"]:
    print(state["name"], state["abbreviation"])
    
    #How can we modify the file from python
    del state["area_codes"]

#Can overwrite the same file but i chose to create a new one
with open('new_data.json', 'w') as f:
    json.dump(data, f, indent=2)