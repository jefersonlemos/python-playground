def get_language(country):
    data = "Usa:English," \
    "Brazil:Portuguese," \
    "Spain:Spanish," \
    "Italy:Italian," \
    "France:French," \
    "Germany:German"
    pairs = data.split(",")
    for p in pairs:
        c, l = p.split(":")
        if c == country:
            return l
        

print(get_language("Italy"))        