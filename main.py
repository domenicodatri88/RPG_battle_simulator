import random

player = {
    "name": "",
    "health": 100,
    "max_health": 100,
    "attack": 20,
    "defense": 10
}

enemy = {
    "name": "Goblin",
    "health": 80,
    "max_health": 80,
    "attack": 15,
    "defense": 8
}

actions = ["Attack", "Heal"]

def initialize_player(player_stat):
    user_name = input("Insert your name: ")
    player_stat["name"] = user_name

def combat_system_player(player, enemy):
    action = input("Pick one option, Attack (A) or Heal (H): ").lower()
    if action == "a":
        damage = player["attack"] - enemy["defense"]
        if damage < 0:
            damage = 0
        print(f"Player attacks with strength = {player['attack']}")
        enemy["health"] -= damage
        if enemy["health"] < 0:
            enemy["health"] = 0
        print(f"Enemy health: {enemy['health']}")
    elif action == "h":
        player["health"] += 10
        if player["health"] > player["max_health"]:
            player["health"] = player["max_health"]
        print(f"Player health: {player['health']}")

def combat_system_enemy(player, enemy, actions):
    action = random.choice(actions)
    if action == "Attack":
        print(f"Enemy decided to {action}")
        damage = enemy["attack"] - player["defense"]
        if damage < 0:
            damage = 0
        player["health"] -= damage
        if player["health"] < 0:
            player["health"] = 0
        print(f"Player health: {player['health']}")
    elif action == "Heal":
        print(f"Enemy decided to {action}")
        enemy["health"] += 10
        if enemy["health"] > enemy["max_health"]:
            enemy["health"] = enemy["max_health"]
        print(f"Enemy health: {enemy['health']}")

game_is_on = True
while game_is_on:
    player["health"] = player["max_health"]
    enemy["health"] = enemy["max_health"]

    print("Welcome to the battle. Here the challengers of today!\n")
    initialize_player(player)
    for key in player:
        print(f"{key}: {player[key]}")
    print("\nAND\n")
    for key in enemy:
        print(f"{key}: {enemy[key]}")

    combat_round = True
    while combat_round:
        combat_system_player(player, enemy)
        if enemy["health"] <= 0:
            print("Enemy is dead, congratulations! YOU WIN")
            combat_round = False
        else:
            combat_system_enemy(player, enemy, actions)
            if player["health"] <= 0:
                print("You died!")
                combat_round = False

    keep_going = input("Do you want to play another round? Type Y or N: ").lower()
    if keep_going == "n":
        game_is_on = False