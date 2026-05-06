import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data for {name}. status code: {response.status_code}")

pokemon_name = input("Enter name of the pokemon: ")
pokemon_info = get_pokemon(pokemon_name)

if pokemon_info:
    print(f"name: {pokemon_info["name"].capitalize()}")
    print(f"id: {pokemon_info["id"]}")
    print(f"height: {pokemon_info["height"]}")
    print(f"weight: {pokemon_info["weight"]}")
    print(f"ability: {pokemon_info["ability"]}")



