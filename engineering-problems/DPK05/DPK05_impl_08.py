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
    1: 0,
    0: "draw",
    -1: 1,
}

POINTS_BY_OUTCOME = {
    "winner": score_rules["winner"],
    "loser": score_rules["loser"],
    "draw": score_rules["draw"],
}


def get_power(player):
    return power.get(player)


def get_most_powerful(player1, player2):
    players = (player1, player2)
    powers = tuple(get_power(player) for player in players)

    if None in powers:
        return None

    comparison = (powers[0] > powers[1]) - (powers[0] < powers[1])
    winner_index = RESULT_BY_COMPARISON[comparison]

    if winner_index == "draw":
        return "draw"

    return players[winner_index]


def add_score(player, outcome):
    leaderboard[player] += POINTS_BY_OUTCOME[outcome]


def update_leaderboard(players, winner):
    if winner == "draw":
        outcomes = ("draw", "draw")
    else:
        outcomes = ("winner", "loser") if players[0] == winner else ("loser", "winner")

    for player, outcome in zip(players, outcomes):
        add_score(player, outcome)


def play(player1, player2):
    players = (player1, player2)
    winner = get_most_powerful(player1, player2)

    if winner is None:
        return None

    update_leaderboard(players, winner)

    return winner


print(play("John", "Paul"))
print(play("John", "Ringo"))
print(leaderboard)
