import json

# Setting the file path for the JSON file and opening it as a json object
path = "C:/Users/Thaddeus/Coding/VS Code/Rotation_Checker/showTVData.json" 
f = open(path, 'r')
rotation_json = json.load(f)

rotation_str = json.dumps(rotation_json, indent=2)

# This block gets the first 4 times inside of 'timeList', as these are the same across each pit
# and saves it as a list
i = 0 
time_list = list()
for model in rotation_json['models']:
    for time in model['timeList']:
        start_time = time['startTimeLocal']
        if i < 4:
            time_list.append(start_time)
        i += 1
        if i == 4:
            break


def table_list():
    for model in rotation_json['models']: #Loop through all pits
        pit_name = model['pitName'] #Put pitname in variable
        print("\nCurrent pit:", pit_name)
        for dealer in model['dealerToTableList']: #Loop through all dealers in all pits
            t = 0 # To initialize time_list variable
            dealer_name = dealer['dealerName'] #Set current dealer name to variable
            print("\nDealer:", dealer_name)
            for table in dealer['tables']:
                    table_value = table['table']
                    print("Table:", table_value, "at", time_list[t]) #print table, and time from time_list
                    t += 1 #

table_list()

# def times():
#     i = 0
#     for model in rotation_json['models']:
#         for time in model['timeList']:
#             start_time = time['startTimeLocal']
#             print(start_time)
#             i += 1
#             if i == 4:
#                 break




#print(rotation_json['models'][0]['dealerToTableList'][0]['tables'][0]['table'])


# for model in rotation_json['models']:
#      for dealer in model['dealerToTableList']:
#           for table in dealer['tables']:
#             table_value = table['table']
#             print(table_value)

#print(rotation_json['models'][0]['timeList'][INTEGER]['startTimeLocal'])