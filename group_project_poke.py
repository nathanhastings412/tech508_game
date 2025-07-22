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

def get_attack_stat(data):
    for stat in data['stats']:
        if stat['stat']['name'] == 'attack':
            return stat['base_stat']
    return 0


player_attack = get_attack_stat(pokemon_data)
cpu_attack = get_attack_stat(cpu_data)

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
print('ability: {}'.format(ability['name']))

print("\n--- CPU Pokémon ---")
print(f"name: {cpu_name}")
print(f"attack {cpu_attack}")
print(f"weight: {cpu_weight}(kgs)")
print(f"height: {cpu_height}(m)")


print("\n--- battle results ---")
print(f"Your Pokémon: {pokemon_data['name'].title()}")
print(f"Your Attack: {player_attack}")
print(f"CPU Pokémon: {cpu_data['name'].title()}")
print(f"CPU Attack: {cpu_attack}")

if player_attack > cpu_attack:
    print("You win!")
elif cpu_attack > player_attack:
    print("CPU wins!")
else:
    print("It's a draw!")