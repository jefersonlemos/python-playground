'''
Approach: Define a list of tuples, iterate over it, if matches, 
return the element of the resulting the list

'''

def get_language(country):
    data = [
        ("Usa","English"),
        ("Brazil","Portuguese"),
        ("Spain","Spanish"),
        ("Italy","Italian"),
        ("France","French"),
        ("Germany","German")
    ]
    return [l for c, l in data if c == country][0]


print(get_language("Brazil"))
