'''
Approach: To be defined
'''

data_map = [
    {"id": 1, "name": "Kuberneide Arantes", "email": "kuberneto@aol.com"},
    {"id": 2, "name": "Javagner da Silva ", "email": "javagner@bol.com"},
    {"id": 3, "name": "Rustina Souza Python", "email": "rusthon@cafecomvenvanse.com"}
]

def lookup(key):

    for item in data_map:
        if isinstance(key, int) and item["id"] == key:
            return item["name"]
        
    
    return None

print(lookup(1))