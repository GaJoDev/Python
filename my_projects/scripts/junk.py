from pathlib import Path
import json

# Path to the JSON file
file_path = Path(r'E:\Dropbox\Python\data_files\rick_morty_data.json')

# Load the data from the file
with file_path.open('r') as file:
    data = json.load(file)

# Define base URL and endpoints (if needed for later use)
baseurl = 'https://rickandmortyapi.com/api/'
character_endpoint = 'character'
location_endpoint = 'location'
episode_endpoint = 'episode'

# Example: Accessing and printing character data from the JSON
if 'character' in data:
    print("Characters:")
    for character in data['character']:
        # Assuming character data has 'name' and 'id'
        print(f"ID: {character.get('id')}, Name: {character.get('name')}")

# Example: Accessing and printing location data from the JSON
if 'location' in data:
    print("\nLocations:")
    for location in data['location']:
        # Assuming location data has 'id' and 'name'
        print(f"ID: {location.get('id')}, Name: {location.get('name')}")

# Example: Accessing and printing episode data from the JSON
if 'episode' in data:
    print("\nEpisodes:")
    for episode in data['episode']:
        # Assuming episode data has 'id' and 'name'
        print(f"ID: {episode.get('id')}, Name: {episode.get('name')}")

