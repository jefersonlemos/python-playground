power = {
    "John": 100,
    "Paul": 90,
    "George": 80,
    "Ringo": 70,
}


def get_power(player):
    return next((power[p] for p in power if p == player), None)


def get_most_powerful(player1, player2):
    p1_power = get_power(player1)
    p2_power = get_power(player2)
    
    if p1_power is None or p2_power is None:
        return None
    
    battle_result = (p1_power > p2_power) - (p1_power < p2_power)
    
    if battle_result == 1:
        return player1
    elif battle_result == -1:
        return player2
    else:
        return None


print(get_most_powerful('John', 'Paul'))
print(get_most_powerful('Paul', 'John'))
print(get_most_powerful('George', 'Ringo'))