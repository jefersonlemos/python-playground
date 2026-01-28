'''
Approach: It creates a list and look up in it
'''

data_map = [
    {"id": 1, "name": "Kuberneide Arantes", "email": "kuberneto@aol.com"},
    {"id": 2, "name": "Javagner da Silva", "email": "javagner@bol.com"},
    {"id": 3, "name": "Rustina Souza Python", "email": "rusthon@cafecomvenvanse.com"}
]

    
def lookup(key, data=None):
    if data is None:
        data = data_map

    if not data:
        return None

    row = data[0]

    if key == row["id"]:
        return row["name"]
    if key == row["name"]:
        return row["email"]
    if key == row["email"]:
        return row["id"]

    return lookup(key, data[1:])

print(lookup(1))
#Returns name
 
print(lookup("Javagner da Silva"))
#Returns email

print(lookup("rusthon@cafecomvenvanse.com"))
#Returns id