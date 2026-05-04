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
    "draw": 5,
}


def get_power(player):
    return power.get(player)
