# https://www.youtube.com/watch?v=-oPuGc05Lxs
# https://rickandmortyapi.com/api

import requests
baseurl = 'https://rickandmortyapi.com/api/'

character_endpoint = 'character'
location_endpoint = 'location'
episode_endpoint = 'episode'


r = requests.get(baseurl + character_endpoint)

print(r)
# print(r.json())

# data = r.json()
# pages = (data['info']['pages'])

# name = (data['results'][0]['name'])
# episodes = (data['results'][0]['episode'])

# print(episodes)
