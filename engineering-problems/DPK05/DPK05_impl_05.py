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

	if power1 > power2:
		return player1
	if power2 > power1:
		return player2
	return "Draw"
