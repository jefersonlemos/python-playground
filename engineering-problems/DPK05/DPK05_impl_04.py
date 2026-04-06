power = {
    "John": 100,
    "Paul": 90,
    "George": 80,
    "Ringo": 70,
}

leaderboard = {
    "John": 0,
    "Paul": 0,
    "George": 0,
    "Ringo": 0,
}


# 1 - search function
def get_power (player, i):
    power_hash_size = len(power)
    players = list(power.keys())
    
    if player == None:
        return "Player None"
        
    if i <= power_hash_size:
        if player == players[i]:
            return power[player]
    else:
        return None

    return get_power(player, i + 1)

# 2 - battle
def battle (battle_players):
    players_list = list(power.keys())
    players_to_battle = []

    if battle_players == None: 
        return None
    
    if len(battle_players) != 2:
        print(len(battle_players))
        return "Num of Players must be 2"
    
    i = 0
    while i < len(battle_players):
        player = battle_players[i]
        if player not in players_list:
            return f"{player} not found"
        players_to_battle.append(player)
        i += 1

    player_1 = players_to_battle[0]
    player_2 = players_to_battle[1]

    player_1_power = get_power(player_1, 0)
    player_2_power = get_power(player_2, 0)

    if player_1_power > player_2_power:
        update_leaderboard(player_1, "winner")
        update_leaderboard(player_2, "loser")
    elif player_2_power > player_1_power:
        update_leaderboard(player_2, "winner")
        update_leaderboard(player_1, "loser")
    else:
        update_leaderboard(player_1, "draw")
        update_leaderboard(player_2, "draw") 
    
    return leaderboard

def update_leaderboard(player, result=None):
    score_values = {
        "winner": 10,
        "loser": -5,
        "draw": 5
    }

    if result == "draw":
        leaderboard[player] -= score_values[result]
    else:
        leaderboard[player] += score_values[result]
    


print(battle(battle_players=["John", "Paul"]))
