import json

# Load the JSON data
with open('rick_morty_api_data/characters.json', 'r') as file:
    data = json.load(file)

# Print the entire structure to inspect
print(json.dumps(data, indent=4))  # Pretty-print the entire JSON with indentation

# Or print the type of the data and some initial details
print(f"Data type: {type(data)}")
print(f"Keys in data: {data.keys()}")

# If the data is a list of results (common for APIs), check a sample
if isinstance(data, dict) and 'results' in data:
    print("\nFirst 2 entries in 'results':")
    print(json.dumps(data['results'][:9], indent=4))  # Show first 2 items for inspection
