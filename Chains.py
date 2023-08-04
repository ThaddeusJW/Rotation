from collections import defaultdict

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

chains = defaultdict()
chain_list = list()


def search(dealer, table):
    for key, values in my_dictionary.items():
        if values[0] == table:
            print(f"{dealer}'s next table is {key}'s current table: {table}")
            dealer_tmp = key
            table_tmp = values[1]
            chain_list.append(table)

            if values[1].startswith("B"):
                print(f"{dealer_tmp} goes to break")
                chain_list.append("Break")
                break
            else:
                search(dealer_tmp, table_tmp)

        else:
            pass
    chains[chain_dealer] = chain_list


for key, values in my_dictionary.items():
    chain_list = list()

    if values[0].startswith("B"):
        chain_dealer = key
        search_table = values[1]
        chain_list.append(values[0])
        chains[chain_dealer] = search_table
        print("\nSearching for chains starting with: ", key)
        search(chain_dealer, search_table)

    else:
        pass

for k, v in chains.items():
    print("-------------\n", k, v)
