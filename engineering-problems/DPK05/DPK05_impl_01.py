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
    if player1_power > player2_power:
        return winner == player1
    elif player1_power == player2_power:
        draw = True
        return draw
    else: 
        return winner == player2
    
    
    
    
    
    
    player1_power = get_power(player1)
    player2_power = get_power(player2)
    winner_score = 10
    draw_score = 5
    loser_score = -5

    return 

    def update_leaderboard(player1, player2): 
            
        for player in leaderboard:
            if player == winner:
                leaderboard[player] += winner_score




def play(player1, player2):
    winner = get_most_powerful(player1, player2)
    
    # leaderboard...
    return winner


print(play("John", "Paul"))
# print(leaderboard)

# print(play("John", "Ringo"))
# print(leaderboard)
