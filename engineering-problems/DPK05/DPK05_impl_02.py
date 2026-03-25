power = {
    "John": 100,
    "Paul": 90,
    "George": 80,
    "Ringo": 70
}

leaderboard = {
    "John": 0,
    "Paul": 0,
    "George": 0,
    "Ringo": 0
}

# 1 busca power - 1
def get_power(player, i):
    if i >= len(power):
        return None
    
    person = list(power.keys())[i]
    if person == player:
        return power[person]
    
    return get_power(player, i+1)
    

print(get_power("Paul", 0))
    
# 2 busca mais forte


# 3 atualiza leaderboard



