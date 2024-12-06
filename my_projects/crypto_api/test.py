import requests
import os
import json

def get_data_set():
    while True:
        # Prompt for the user option
        user_option = input("[1] for API request or [2] for existing data list | ")

        # Check if input is a digit
        if user_option.isdigit():
            opt_to_int = int(user_option)  # Convert to an integer
            if opt_to_int >= 1 and opt_to_int <= 2:  # Check if within valid range
                return opt_to_int  # Return valid input
            else:
                print("Not a valid choice. Please select 1 or 2.")
        else:
            print("NAN")
            
def load_data(result):
    if result == 1:
        # API request code here
        print("api_get option reached",result)
        print("APT GET OPTION: data_list from the URL...")
        # Fetch new data_list if no cache
        response = requests.get(url)
        data_list = response.json()

        print("saving list to data_list_cache.json")
        # Cache the data_list for future use
        with open("data_list_cache.json", "w") as file:
            json.dump(data_list, file)
        
        return data_list
        
    elif result == 2:
        # existing data list code here
        print("LOADING CACHED FILE: data_list_cache.json")
        os.path.exists("data_list_cache.json")
        with open("data_list_cache.json", "r") as file:
            data_list = json.load(file)
        print("Using cached data_list...")
        print(type(data_list))

        return data_list

        # Fetch new data_list if no cache
        # response = requests.get(url)
        # data_list = response.json()

        # # Cache the data_list for future use
        # with open("data_list_cache.json", "w") as file:
        #     json.dump(data_list, file)
        # print("Fetching new data_list from the URL...")


        # # Call the function and capture the returned value
        # option = get_data_set()
        # print("This was the value passed from the function:", option)
        # load_data(option)

def process_data_list(data_list):
    for x in range(0, 5):
    # identify a record
        print("----------------")
        print("Rank",json.dumps(data_list[x]['rank'], indent=4), end=" | ")
        print("Symbol",json.dumps(data_list[x]['symbol'], indent=4), end=" | ")
        print("Price",json.dumps(data_list[x]['quotes']['USD']['price']), end=" | ")
        # print("Last price update:",json.dumps(data_list[x]['last_updated']))
        # print("----------------")

url = "https://api.coinpaprika.com/v1/tickers"

result = get_data_set()
data_list =load_data(result)
process_data_list(data_list)


