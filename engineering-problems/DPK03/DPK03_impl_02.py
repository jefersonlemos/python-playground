'''
Approach: Search the given key by iteratng over the map using a while loop, getting index and keys and comparing the values
'''

data_map = [
    {"id": 1, "name": "Kuberneide Arantes", "email": "kuberneto@aol.com"},
    {"id": 2, "name": "Javagner da Silva", "email": "javagner@bol.com"},
    {"id": 3, "name": "Rustina Souza Python", "email": "rusthon@cafecomvenvanse.com"}
]

def lookup(key):
    i = 0 
    while i < len(data_map):
        if data_map[i].get("id") == key:
            return data_map[i].get("name")
        
        if data_map[i].get("name") == key:
            return data_map[i].get("email")
        
        if data_map[i].get("email") == key:
            return data_map[i].get("id")                
        i += 1

    return None

#Returns name
print(lookup(1))
#Returns email 
print(lookup("Javagner da Silva"))
#Returns id
print(lookup("rusthon@cafecomvenvanse.com"))