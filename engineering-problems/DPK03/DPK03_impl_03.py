'''
Approach: Lookup the map using recursion
'''

data_map = [
    {"id": 1, "name": "Kuberneide Arantes", "email": "kuberneto@aol.com"},
    {"id": 2, "name": "Javagner da Silva", "email": "javagner@bol.com"},
    {"id": 3, "name": "Rustina Souza Python", "email": "rusthon@cafecomvenvanse.com"}
]
i = 0
def lookup(key, i = 0 ):
    if i >= len(data_map):
        return None
        
    if data_map[i]["id"] == key:
        return data_map[i]["name"]
        
    if data_map[i]["name"] == key:
        return data_map[i]["email"]
                    
    if data_map[i]["email"] == key:
        return data_map[i]["id"]
    
    
    return lookup(key, i + 1)


print(lookup(1))
#Returns name
 
print(lookup("Javagner da Silva"))
#Returns email

print(lookup("rusthon@cafecomvenvanse.com"))
#Returns id