power = {
    "John": 100,
    "Paul": 90,
    "George": 80,
    "Ringo": 70
}

leaderboard = {
    "John": 0,
    "Paul": 0,
    "George": 0,
    "Ringo": 0
}

# 1 busca power - 1
def get_power(player, i):
    if i >= len(power):
        return None
    
    person = list(power.keys())[i]
    if person == player:
        return power[person]
    
    return get_power(player, i+1)
    

# 2 busca mais forte
def get_most_powerful(player1, player2):
    power1 = get_power(player1, 0)
    power2 = get_power(player2, 0)

    if power1 == power2:
        return None

    if power1 >= power2:
        return player1

    return player2

# 3 atualiza leaderboard
def play(player1, player2):

    winner = get_most_powerful(player1, player2)
    if winner is not None:
        loser = player2 if winner == player1 else player1
        leaderboard[winner] += 10
        leaderboard[loser] -= 5
    else:
        leaderboard[player1] += 5
        leaderboard[player2] += 5
    return leaderboard
    

print(play("John", "Ringo"))
print(play("John", "George"))


