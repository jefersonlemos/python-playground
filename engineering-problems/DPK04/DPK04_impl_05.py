def get_language(country, data=None, i=0):
    if data is None:
        data = [
            ("Usa","English"),
            ("Brazil","Portuguese"),
            ("Spain","Spanish"),
            ("Italy","Italian"),
            ("France","French"),
            ("Germany","German")
        ]
    if i >= len(data):
        return None
    c, l = data[i]
    if c == country:
        return l
    return get_language(country, data, i+1)