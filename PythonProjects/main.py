import requests

HOST = 'https://pokemonbattle.me:9104/'
TOKEN = 'token'

response = requests.post(f'{HOST}pokemons', headers ={'trainer_token':TOKEN}, json={
    "name": "Бульбазаврик 3000",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print(response.json())

response = requests.put(f'{HOST}pokemons', headers ={'trainer_token':TOKEN}, json={
    "pokemon_id": "12211",
    "name": "Мега бульбазаврик",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})

print(response.json())

response = requests.post(f'{HOST}trainers/add_pokeball', headers ={'trainer_token':TOKEN}, json={
    "pokemon_id": "12211"
})

print(response.json())
