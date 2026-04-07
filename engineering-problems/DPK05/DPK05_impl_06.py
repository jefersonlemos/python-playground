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
    battle_result = [None] * len(players)
    i = 0
    for player in players:
        battle_result[i] = (player, get_power(player))
        i += 1
        
    return battle_result



players = ["Ringo", "John"]
print(battle(players))
