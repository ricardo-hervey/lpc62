import requests

def get_all_pokemon_names():
    base_url = "https://pokeapi.co/api/v2/"
    endpoint = "pokemon-form/"
    url = f"{base_url}{endpoint}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_names = [entry['name'] for entry in data['results']]
        return pokemon_names
    else:
        print(f"Error: {response.status_code}")
        return []

if __name__ == "__main__":
    pokemon_names = get_all_pokemon_names()

    if pokemon_names:
        print("Nombres de todos los Pokémon:")
        for name in pokemon_names:
            print(name)
    else:
        print("No se pudo obtener la lista de nombres de Pokémon.")
