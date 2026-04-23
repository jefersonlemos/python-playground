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

score = {
    "winner": 10,
    "loser": -5,
    "draw": 5,
}

def get_power(player):
    return next((power[p] for p in power if p == player), None)


def get_most_powerful(player1, player2):
    p1_power = get_power(player1)
    p2_power = get_power(player2)
    
    if p1_power is None or p2_power is None:
        return None
    
    battle_result = (p1_power > p2_power) - (p1_power < p2_power)
    
    if battle_result == 1:
        return update_leaderboard(player1)
    elif battle_result == -1:
        return update_leaderboard(player2)
    else:
        return update_leaderboard(None)

def update_leaderboard(winner):
    if winner is None:
        winner = "draw"

    for player in leaderboard:
        if winner == player:
            leaderboard[player] += score[winner]

print(get_most_powerful('John', 'Paul'))
print(get_most_powerful('Paul', 'John'))
print(get_most_powerful('George', 'Ringo'))