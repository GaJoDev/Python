import requests
import json

baseurl = 'https://rickandmortyapi.com/api/'

def fetch_index_data():
    # Fetch the main API index
    index_url = baseurl
    response = requests.get(index_url)
    data = response.json()

    # Save the index data (which contains URLs for characters, locations, and episodes)
    with open('api_index.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("API index data saved locally!")

fetch_index_data()

def fetch_and_save_data_from_index():
    # Load the API index data (which contains the URLs for the actual data)
    with open('api_index.json', 'r') as f:
        index_data = json.load(f)

    # Fetch data from each endpoint
    character_url = index_data['characters']
    location_url = index_data['locations']
    episode_url = index_data['episodes']

    # Fetch each resource and save the data locally
    characters = requests.get(character_url).json()
    locations = requests.get(location_url).json()
    episodes = requests.get(episode_url).json()

    # Save data locally
    with open('characters.json', 'w') as f:
        json.dump(characters, f, indent=4)

    with open('locations.json', 'w') as f:
        json.dump(locations, f, indent=4)

    with open('episodes.json', 'w') as f:
        json.dump(episodes, f, indent=4)

    print("Data fetched from the API and saved locally!")

fetch_and_save_data_from_index()

