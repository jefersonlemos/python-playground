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
    is_match = True
    while i < len(battle_players):
        for player in battle_players:
            for player_from_list in players_list:
                if player == player_from_list:
                    i += 1
                elif i < 1 and player != player_from_list:
                    return f"{player} not found"
                    next
                elif i == 1 and player != player_from_list:
                    i += 1
                    return f"{player} not found"

        


def play(players):
    # return get_power(player,0)
    return battle(battle_players=players)

print(play(players=["John", "Marcio"]))
