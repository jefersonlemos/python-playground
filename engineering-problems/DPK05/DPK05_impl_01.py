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

def get_power(name):
    for person in power:
        if person == name:
            return power[person]
    return None

def get_most_powerful(player1, player2):
    winner = None
    loser = None
    draw = True

    player1_power = get_power(player1)
    player2_power = get_power(player2)
    
    if player1_power != player2_power: 
        if player1_power > player2_power:
            winner = player1
            draw = False
        else: 
            winner = player2
            draw = False
    
    if not draw:
        if winner == player1: 
            loser = player2
        else: 
            loser = player1

        leaderboard[winner] += 10
        leaderboard[loser] -= 5
    else: 
        leaderboard[player1] += 5
        leaderboard[player2] += 5
        
    return leaderboard 

def play(player1, player2):
    winner = get_most_powerful(player1, player2)
    
    # leaderboard...
    return winner


print(play("John", "Paul"))
# print(leaderboard)

# print(play("John", "Ringo"))
# print(leaderboard)
