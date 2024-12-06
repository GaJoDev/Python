
# ============VERSION 1============
# ''''''
import requests
import json

# set the variable url to be equal to contents of the get request to the api
url = requests.get('https://api.coinpaprika.com/v1/tickers')

# Prints the status code from the api request - 200 shows that it is a valid request
# print("status_code received : ", (url))

# a variable to hold the data object retrieved from the api parsed from json
data_list = url.json()

# print(data_list) limiting the output to 5 items
for x in range(0, 40):
        print("Rank",json.dumps(data_list[x]['rank'], indent=4), end=" : ")
        print("Symbol",json.dumps(data_list[x]['symbol'], indent=4), end=" : ")
        print("Price",json.dumps(data_list[x]['quotes']['USD']['price']))  
    



# Prints out a formatted list of the data retrieved from the api
# print(json.dumps(data_list, indent=4))

# Outputs the number of records in the reponse list
# print("Number of records in the list: ", len(data_list))

# this was used just to demonstrate that the json is being returned - it's not necessary for the rest of the code as it prints out the entire list
# print(url.json())

# This prints out the first record in the list
# print(data_list[0])
# This prints out the relevant 'key' in the list - need to work out how to access its value
# print(data_list[0]['id'])

# noticed that 'quotes' value is another list and that 'USD' value is another dictionary within that list and price is a key from the lowest level of recursion
# print(data_list[0]['quotes']['USD']['price'])

# # and so is 'USD' within the 'quotes list'
# print(data_list[0]['USD'])

# Slowly getting there, it lists the keys list and the values list within a record, just need to get these to relate to each other and print out
# https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
# https://www.codecademy.com/learn/dscp-python-fundamentals/modules/dscp-python-dictionaries/cheatsheet
# https://learnpython.com/blog/python-list-loop/
data_key_list = list(data_list[0].keys())
data_value_list = list(data_list[0].values())
data_item_list = list(data_list[x].items())
# print(f"Keys: {key_list}")
# print("Values: {value_list})

# print(f"Items: {data_item_list}")

# print(len(data_list))
# list_length = len(data_list)
# print(f"There are {list_length} Records in the list")


# print(type(data_list))
# ''''''
# ============end VERSION 1============

# ============VERSION 2============
# #This Version is the chatgpt solution, lets see if this works

# import requests

# # URL for the API endpoint (Replace with the actual URL you are calling)
# url = 'https://api.coinpaprika.com/v1/tickers'

# # Make the API call
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON data from the response
#     data = response.json()
    
#     # If the response is a list, iterate through the list
#     if isinstance(data, list):
#         for item in data:
#             print(item)  # Prints each item in the list
#     elif isinstance(data, dict):
#         # If the response is a dictionary, iterate through the keys and values
#         for key, value in data.items():
#             print(f"Key: {key}, Value: {value}")
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")

# ============VERSION 2============

#random hacking attempts
# for testing, this just prints out the first record
# print(data[0])

# this converts the data variable from a list to a string
# list_to_string = str(data)
# print(list_to_string[0:5])
# print(type(list_to_string))

# Found this on stack overflow:
# https://stackoverflow.com/questions/77827572/converting-json-list-from-an-api-into-a-python-dictionary
# data_list = json.dumps(list_to_string)

# data_list = requests.get(url).json()

# print("data_list is the current class: ", type(data_list))

# key_list = list(data_list.keys())

# position = key_list.index(0, 5)
# print(key_list[position])
# # for id in range (1, 30):
# #     # print(id, ":", data_list[0])
# #     print(data_list[3:29])
