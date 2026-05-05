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

LOSER_POINTS = -5
WINNER_BONUS = 15
DRAW_BONUS = 10


def get_power(player):
    for name in power:
        if name == player:
            return power[name]
    return None


def get_most_powerful(player1, player2):
    player1_power = get_power(player1)
    player2_power = get_power(player2)

    if player1_power is None or player2_power is None:
        return None

    if player1_power > player2_power:
        return player1

    if player2_power > player1_power:
        return player2

    return "draw"


def add_points(player, points):
    leaderboard[player] = leaderboard[player] + points


def apply_winner(player1, player2, winner):
    add_points(winner, WINNER_BONUS)


def apply_draw(player1, player2, winner):
    add_points(player1, DRAW_BONUS)
    add_points(player2, DRAW_BONUS)


def play(player1, player2):
    winner = get_most_powerful(player1, player2)

    if winner is None:
        return None

    add_points(player1, LOSER_POINTS)
    add_points(player2, LOSER_POINTS)

    result_actions = {
        player1: apply_winner,
        player2: apply_winner,
        "draw": apply_draw,
    }

    result_actions[winner](player1, player2, winner)

    return winner


print(play("John", "Paul"))
# print(play("John", "Ringo"))
print(leaderboard)
