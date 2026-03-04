def get_language(country):
    data = [
        ("Usa", "English"),
        ("Brazil", "Portuguese"),
        ("Spain", "Spanish"),
        ("Italy", "Italian"),
        ("France", "French"),
        ("Germany", "German")
    ]
    
    def search_language(index):
        if index >= len(data):
            return None
        
        current_country = data[index][0]
        current_language = data[index][1]
        
        if compare_country(current_country, country):
            return current_language
        
        return search_language(index + 1)
    
    return search_language(0)

def compare_country(current_country, country):
    if current_country != country:
        return False
    return country

print(get_language("Brazil"))
print(get_language("Germany"))
# print(get_language("Italy"))
