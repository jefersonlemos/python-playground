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

score_rules = {
    "winner": 10,
    "loser": -5,
    "draw": 5
}


def get_power(player):
    if player in power:
        return power[player]
    return None


def battle(players):
    battle_results = [None] * len(players)
    i = 0
    for player in players:
        battle_results[i] = (player, get_power(player))
        i += 1

    i = 0
    for i in range(2):
        if i == 0:
            next_player_power = battle_results[i + 1][1]
            current_power = battle_results[i][1]
        else:
            next_player_power = battle_results[i - 1][1]
            current_power = battle_results[i][1]
        
        if current_power > next_player_power:
            battle_results[i] = (battle_results[i][0], battle_results[i][1], "winner")
        elif current_power == next_player_power:
            battle_results[i] = (battle_results[i][0], battle_results[i][1], "draw")
        else:
            battle_results[i] = (battle_results[i][0], battle_results[i][1], "loser")

    return battle_results

        i += 1

# def update_leaderboard(battle_results):
    
    # battle_results

    # return leaderboard


players = ["John", "Ringo"]
print(battle(players))
