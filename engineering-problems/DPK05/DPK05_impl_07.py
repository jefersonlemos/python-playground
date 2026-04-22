power = {
    "John": 100,
    "Paul": 90,
    "George": 80,
    "Ringo": 70,
}


def get_power(player):
    return next((power[p] for p in power if p == player), None)


print(get_power('John'))