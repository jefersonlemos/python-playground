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

RESULT_BY_COMPARISON = {
    1: "player1",
    0: "draw",
    -1: "player2",
}

def get_power(player):
    return power.get(player)


def get_most_powerful(player1, player2):
    player1_power = get_power(player1)
    player2_power = get_power(player2)

    if player1_power is None or player2_power is None:
        return None

    comparison = (player1_power > player2_power) - (player1_power < player2_power)
    result = RESULT_BY_COMPARISON[comparison]

    winners_by_result = {
        "player1": player1,
        "player2": player2,
        "draw": "draw",
    }

    return winners_by_result[result]


print(get_most_powerful("John","Paul"))