from collections import defaultdict

# Dictionary of the JSON file. Don't need to re-invent the wheel
my_dictionary = {
    "Babala Bowling": ["6470", "B", "6435", "6424"],
    "Crawfish Corey": ["SH 5", "6474", "6437", "6470"],
    "Daniel Day-Lewis": ["6435", "6424", "Break", "SH 5"],
    "Willie Free": ["6437", "6470", "B", "6435"],
    "Marmite Mass": ["6474", "6437", "6470", "B"],
    "Shack Love": ["6424", "Break", "SH 5", "6474"],
    "Hotel Habbo": ["B", "6435", "6424", "Break"],
    "Shook Tree": ["Break", "SH 5", "6474", "6437"],
}

# Create defaultdict since we dont know how many chains we'll have
chains = defaultdict()


# Recursive function time taking the chain starting dealer and their table
def search(dealer, table):
    # Iterating through every dealer to see if their current table is the chain_dealer's next table
    for key, values in my_dictionary.items():
        # If the current iterations 0th table is chain_dealers 1st table
        if values[0] == table:
            print(f"{dealer}'s next table is {key}'s current table: {table}")

            # Storing the dealer name and table as temporary values to pass later
            dealer_tmp = key
            table_tmp = values[1]

            # Append the chain_list with the table number we searched for in the chain
            chain_list.append(table)

            # To prevent infinite loops, need to break the chain when we find the next dealer on break
            if values[1].startswith("B"):
                print(f"{dealer_tmp} goes to break")
                chain_list.append("Break")
                break

            # Redo the loop with the dealer/table we just found
            else:
                search(dealer_tmp, table_tmp)

        else:
            pass

    # Once we've made it through the loop append the list we've made
    # to the chain_dealers key so we have all tables in the chain
    chains[chain_dealer] = chain_list


# For loop to find out who is going to be coming back from Break
for key, values in my_dictionary.items():
    # Making a blank chain_list list every time we find a dealer from break
    chain_list = list()

    # We're taking the name of the dealer to find out who starts the chain
    # and their table number so we know what table to search for next
    if values[0].startswith("B"):
        chain_dealer = key
        search_table = values[1]
        chain_list.append(values[0])
        chains[chain_dealer] = search_table
        print("\nSearching for chains starting with: ", key)

        # Then pass it into the search function
        search(chain_dealer, search_table)

    else:
        pass

for k, v in chains.items():
    print("-------------\n", k, v)
