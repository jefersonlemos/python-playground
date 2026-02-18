'''
Approach: Defines a list of tuples and iterate over it
'''

def get_language(country):
    data = [
        ("Usa", "English"), 
        ("Brazil", "Portuguese"), 
        ("Spain", "Spanish"),
        ("Italy", "Italian"),
        ("France", "French"), 
        ("Germany", "German")
    ]

    for c, l in data:
        if c == country:
            return l

print(get_language("Brazil"))
print(get_language("Germany"))