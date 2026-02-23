'''
Approach: Create a brazil list and the language will be on another list in the same index
'''

def get_language(country):
    countries = ["Usa","Brazil","Spain","Italy","France","Germany"]
    languages = ["English","Portuguese","Spanish","Italian","French","German"]
    i = countries.index(country)
    return languages[i]


print(get_language("Brazil"))