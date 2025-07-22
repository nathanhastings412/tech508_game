import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

cpu_id = random.randint(1,151)
cpu_url = f"https://pokeapi.co/api/v2/pokemon/{cpu_id}/"
cpu_response = requests.get(cpu_url)
cpu_data = cpu_response.json()
cpu_name = cpu_data["name"]
cpu_height = int(cpu_data['height']) / 10
cpu_weight = int(cpu_data['weight']) / 10

def get_stat(data, stat_name):
    """
    Helper function to get a specific stat from pokemon data.
    """
    for stat in data["stats"]:
        if stat['stat']['name'] == stat_name:
            return stat['base_stat']
    return 0

# Get stats for player and CPU
player_attack = get_stat(pokemon_data, "attack")
cpu_attack = get_stat(cpu_data, "attack")
player_defense = get_stat(pokemon_data, "defense")
cpu_defense = get_stat(cpu_data, "defense")
player_speed = get_stat(pokemon_data, "speed")
cpu_speed = get_stat(cpu_data, "speed")

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('name: {}'.format(pokemon_data['name']))
print('weight: {}'.format(weight_formatted) + "(kgs)")
print('height: {}'.format(height_formatted) + "(m)")
print(f"Your Attack: {player_attack}")
print(f"Your Defense: {player_defense}")
print(f"Your Speed: {player_speed}")
print('ability: {}'.format(ability['name']))

print("\n   CPU Pokemon    ")
print(f"name: {cpu_name}")
print(f"attack: {cpu_attack}")
print(f"defense: {cpu_defense}")
print(f"speed: {cpu_speed}")
print(f"weight: {cpu_weight}(kgs)")
print(f"height: {cpu_height}(m)")


print("\n    battle results   ")
print(f"Your Pokémon: {pokemon_data['name'].title()}")
print(f"Your Attack: {player_attack}")
print(f"Your Defense: {player_defense}")
print(f"Your Speed: {player_speed}")
print(f"CPU Pokémon: {cpu_data['name'].title()}")
print(f"CPU Attack: {cpu_attack}")
print(f"CPU Defense: {cpu_defense}")
print(f"CPU Speed: {cpu_speed}")

# Simple battle logic based on combined stats
player_total_power = player_attack + player_defense + player_speed
cpu_total_power = cpu_attack + cpu_defense + cpu_speed

if player_total_power > cpu_total_power:
    print(f"{pokemon_data['name'].title()} wins!")
elif cpu_total_power > player_total_power:
    print(f"{cpu_data['name'].title()} wins!")
else:
    print("It's a draw!")