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


def get_power(player):
    return power.get(player)


def get_most_powerful(player1, player2):
    power1 = get_power(player1)
    power2 = get_power(player2)

    if power1 is None or power2 is None:
        return None

    if power1 == power2:
        return None
    if power1 > power2:
        return player1
    return player2


def play(player1, player2):
    winner = get_most_powerful(player1, player2)
    if winner is None:
        # Draw or invalid input: award draw points only when both players exist.
        if get_power(player1) is None or get_power(player2) is None:
            return None
        leaderboard[player1] += 5
        leaderboard[player2] += 5
        return None

    loser = player2 if winner == player1 else player1
    leaderboard[winner] += 10
    leaderboard[loser] -= 5

    return winner


print(play("John", "Paul"))
print(leaderboard)
print(play("John", "Ringo"))
print(leaderboard)
