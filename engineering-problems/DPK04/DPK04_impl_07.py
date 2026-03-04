data = [
            ("Usa","English"),
            ("Brazil","Portuguese"),
            ("Spain","Spanish"),
            ("Italy","Italian"),
            ("France","French"),
            ("Germany","German")
        ]



def get_language(country):
    for c, l in data:
        if c == country:
            return l
        

def get_language()            
        

print(get_language("Italy"))