'''
Approach: Define and Write down the approach
'''

data_map = [
    {"id": 1, "name": "Kuberneide Arantes", "email": "kuberneto@aol.com"},
    {"id": 2, "name": "Javagner da Silva", "email": "javagner@bol.com"},
    {"id": 3, "name": "Rustina Souza Python", "email": "rusthon@cafecomvenvanse.com"}
]

def find_and_return(key):
    for record in data_map:
        if record["id"] == key:
            return record["name"]
        if record["name"] == key:
            return record["email"]
        if record["email"] == key:
            return record["id"]
    return None

def lookup(key):
    result = find_and_return(key)
    return result

print(lookup(1))
# Returns name
 
print(lookup("Javagner da Silva"))
# Returns email

print(lookup("rusthon@cafecomvenvanse.com"))
# Returns id
