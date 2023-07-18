import json

# Setting the file path for the JSON file and opening it as a json object
path = "C:/Users/Thaddeus/Coding/VS Code/Rotation_Checker/showTVData.json" 
f = open(path, 'r')
rotation_json = json.load(f)

rotation_str = json.dumps(rotation_json, indent=2)


def table_list():
    for model in rotation_json['models']: #Loop through all pits
        for dealer in model['dealerToTableList']: #Loop through all dealers in all pits
            dealer_name = dealer['dealerName'] #Set current dealer name to variable
            print(dealer_name) 

    
table_list()
