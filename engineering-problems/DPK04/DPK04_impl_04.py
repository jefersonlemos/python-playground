'''
Approach: A recursive function that iterates over the list and in each recursive call
 drops the current first element(0)
'''
def get_language(country, data=None):
    if data is None:
        data = [
            ("Usa","English"),
            ("Brazil","Portuguese"),
            ("Spain","Spanish"),
            ("Italy","Italian"),
            ("France","French"),
            ("Germany","German")
        ]
    c, l = data[0]
    if c == country:
        return l
    return get_language(country, data[1:])


print(get_language("Brazil"))