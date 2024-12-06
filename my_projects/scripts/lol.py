
# =====VERSION 1=====
# '''
import requests
# import json

url = requests.get('https://api.coinpaprika.com/v1/tickers')

# print(url.json())
# this was used just to demonstrate that the json is being returned - it's not necessary for the rest of the code as it prints out the entire list


json_data = url.json()
# This prints out the first record in the list
# print(json_data[0])
# This prints out the relevant 'key' in the list - need to work out how to access its value
print(json_data[0]['id'])

# noticed that 'quotes' value is another list and that 'USD' value is another dictionary within that list
# print(json_data[0]['quotes']['USD'])

# # and so is 'USD' within the 'quotes list'
# print(json_data[0]['USD'])

# This is getting there, it lists the keys within a record
# https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
keyslist = list(json_data[0].keys())
print("keyslist:", keyslist)

# print(len(json_data))
# list_length = len(json_data)
# print(f"There are {list_length} Records in the list")


# print(type(json_data))
# '''first attempt, this at least gets the data, but it's not in the format we want'''
# =====VERSION 1=====

# =====VERSION 2=====
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

# =====VERSION 2=====

#random hacking attempts
# for testing, this just prints out the first record
# print(data[0])

# this converts the data variable from a list to a string
# list_to_string = str(data)
# print(list_to_string[0:5])
# print(type(list_to_string))

# Found this on stack overflow:
# https://stackoverflow.com/questions/77827572/converting-json-list-from-an-api-into-a-python-dictionary
# json_data = json.dumps(list_to_string)

# json_data = requests.get(url).json()

# print("json_data is the current class: ", type(json_data))

# key_list = list(json_data.keys())

# position = key_list.index(0, 5)
# print(key_list[position])
# # for id in range (1, 30):
# #     # print(id, ":", json_data[0])
# #     print(json_data[3:29])
