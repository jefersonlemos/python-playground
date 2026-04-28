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


def get_most_powerful(player1, player2):
    player1_power = get_power(player1)
    player2_power = get_power(player2)

    if player1_power is None or player2_power is None:
        return None

    result_by_comparison = {
        1: player1,
        0: "draw",
        -1: player2,
    }

    comparison = (player1_power > player2_power) - (player1_power < player2_power)
    return result_by_comparison[comparison]


def play(player1, player2):
    winner = get_most_powerful(player1, player2)

    if winner is None:
        return None

    score_updates = {
        player1: score_rules["draw"],
        player2: score_rules["draw"],
    }

    if winner != "draw":
        loser = player2 if winner == player1 else player1
        score_updates = {
            winner: score_rules["winner"],
            loser: score_rules["loser"],
        }

    for player, points in score_updates.items():
        leaderboard[player] += points

    return winner


print(play("John", "Paul"))
print(play("John", "Ringo"))
print(leaderboard)
