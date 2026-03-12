def get_language(country):
    data = [
        ("Usa", "English"),
        ("Brazil", "Portuguese"),
        ("Spain", "Spanish"),
        ("Italy", "Italian"),
        ("France", "French"),
        ("Germany", "German")
    ]
    
    index = 0
    while index < len(data):
        if data[index][0] == country:
            return data[index][1]
        index += 1
    
    return None

print(get_language("Brazil"))
print(get_language("Italy"))
