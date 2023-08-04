import json
import pandas as pd

# Setting the file path for the JSON file and opening it as a json object
path = "C:/Users/Thaddeus/Coding/VS Code/Rotation_Checker/showTVData-OnePit.json"
f = open(path, "r")
rotation_json = json.load(f)

rotation_str = json.dumps(rotation_json, indent=2)

# This block gets the first 4 times inside of 'timeList', as these are the same across each pit
# and saves it as a list
i = 0
time_list = list()
for model in rotation_json["models"]:
    for time in model["timeList"]:
        start_time = time["startTimeLocal"]
        if i < 4:
            time_list.append(start_time)
        i += 1
        if i == 4:
            break


# Step 1: Open the JSON file
with open("showTvData-OnePit.json", "r") as file:
    data = json.load(file)

# Step 2: Extract the required data from the JSON
dealer_data = data["models"][0]["dealerToTableList"]
dealer_list = []
tables_list = []

# Step 3: Loop through the dealer list to get all dealers
for dealer in dealer_data:
    dealer_list.append(dealer["dealerName"])

# Step 4: Loop through each dealer
for dealer in dealer_data:
    # To get each table for each dealer
    for table in dealer["tables"]:
        # 'B' break and BREAKS are different, and are marked as null. Gotta catch those
        if table["table"] is None:
            tables_list.append("Break")
        else:
            tables_list.append(table["table"])

dealerTable_dict = {
    dealer_list[i]: tables_list[i * 4 : i * 4 + 4] for i in range(len(dealer_list))
}


def pit():
    # Step 1: Open the JSON file
    with open("showTvData-OnePit.json", "r") as file:
        data = json.load(file)

    # Step 2: Extract the required data from the JSON
    dealer_data = data["models"][0]["dealerToTableList"]
    time_data = data["models"][0]["timeList"]
    dealer_list = []
    time_list = []
    tables_list = []
    counter = 0

    # Step 3: Loop through time list to get the current time schedule
    for time in time_data:
        time_list.append(time["startTimeLocal"])

    # Step 4: Loop through the dealer list to get all dealers
    for dealer in dealer_data:
        dealer_list.append(dealer["dealerName"])

    # Step 5: Loop through each dealer
    for dealer in dealer_data:
        # To get each table for each dealer
        for table in dealer["tables"]:
            # 'B' break and BREAKS are different, and are marked as null. Gotta catch those
            if table["table"] is None:
                tables_list.append("Break")
            else:
                tables_list.append(table["table"])

    # Step 6: Creating a dictionary - Dealer as key, 4 tables as list value
    dealerTable_dict = {
        dealer_list[i]: tables_list[i * 4 : i * 4 + 4] for i in range(len(dealer_list))
    }

    # Step 7: Create a dataframe using the newly created dictionary with the time_list as the columns
    df = pd.DataFrame.from_dict(dealerTable_dict, orient="index", columns=time_list)

    # 7 Step 8: Print the dataframe
    print(df)

    file.close


def rot_chains():
    # Step 1: Open the JSON file
    with open("showTvData-OnePit.json", "r") as file:
        data = json.load(file)

    # Step 2: Extract the required data from the JSON
    dealer_data = data["models"][0]["dealerToTableList"]
    dealer_list = []
    tables_list = []

    # Step 3: Loop through the dealer list to get all dealers
    for dealer in dealer_data:
        dealer_list.append(dealer["dealerName"])

    # Step 4: Loop through each dealer
    for dealer in dealer_data:
        # To get each table for each dealer
        for table in dealer["tables"]:
            # 'B' break and BREAKS are different, and are marked as null. Gotta catch those
            if table["table"] is None:
                tables_list.append("Break")
            else:
                tables_list.append(table["table"])

    dealerTable_dict = {
        dealer_list[i]: tables_list[i * 4 : i * 4 + 4] for i in range(len(dealer_list))
    }

    # Find dealers with B, Break, or Shuffle as their current table
    # to find the start of the chain
    chain_starters = {
        key: values
        for key, values in dealerTable_dict.items()
        if values[0].startswith(("B"))
    }

    # Make a dictionary for all remaining dealers

    chain_remainders = {
        key: values
        for key, values in dealerTable_dict.items()
        if not values[0].startswith("B")
    }

    print("Chain Starters", list(chain_starters.keys()))
    print("Remainders:", list(chain_remainders.keys()))

    for key, values in chain_remainders.items():
        print(key, values)

    for key, values in chain_starters.items():
        print(key, values)


pit()
print("===========================")
rot_chains()
