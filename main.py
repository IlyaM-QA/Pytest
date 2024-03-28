import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'TRAINER_TOKEN'
HEADERS = {'Content-Type' : 'application/json',
           "trainer_token" : TOKEN}

# Созднаие покемона Post

body =  {
    
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)

print(response.text)

# Изменение покемона PUT

body =  {
    "pokemon_id": "14673",
    "name": "Вася",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body)

print(response.text)

# Поймать покемона в покебол POST

body =  {
    "pokemon_id": "14968"
}

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body)

print(response.text)