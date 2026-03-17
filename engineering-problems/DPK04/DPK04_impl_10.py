def get_language(country, data=None, index=0):
    if data is None:
        data = [
            ("Brazil","Portuguese"),
            ("Usa","English"),
            ("Spain","Spanish"),
            ("Italy","Italian"),
            ("France","French"),
            ("Germany","German")
        ]
    if index >= len(data):
        return None
    _country, _language = data[index]
    if _country == country:
        return _language
    return get_language(country, data, index+1)



print(get_language("Italy"))