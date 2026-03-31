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


def play(player):
    return get_power(player,0)

print(play("John"))
