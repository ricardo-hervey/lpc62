import requests

def get_pokemon_list(url):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_names = [entry['name'] for entry in data['results']]
        next_page = data['next']
        return pokemon_names, next_page
    else:
        print(f"Error: {response.status_code}")
        return [], None

def main():
    base_url = "https://pokeapi.co/api/v2/"
    endpoint = "pokemon-form/"
    url = f"{base_url}{endpoint}"

    while url:
        pokemon_names, url = get_pokemon_list(url)

        if pokemon_names:
            print("Nombres de Pokémon:")
            for name in pokemon_names:
                print(name)
        else:
            print("No se pudo obtener la lista de nombres de Pokémon.")
            break

        user_input = input("¿Desea continuar viendo más Pokémon? (s/n): ")
        if user_input.lower() != 's':
            break

if __name__ == "__main__":
    main()
