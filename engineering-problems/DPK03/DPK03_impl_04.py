'''
Approach: Define and Write down the approach
'''

data_map = [
    {"id": 1, "name": "Kuberneide Arantes", "email": "kuberneto@aol.com"},
    {"id": 2, "name": "Javagner da Silva", "email": "javagner@bol.com"},
    {"id": 3, "name": "Rustina Souza Python", "email": "rusthon@cafecomvenvanse.com"}
]

index = {}

for row in data_map:
    index[row["id"]] = row
    index[row["name"]] = row
    index[row["email"]] = row
    
def lookup(key):
    row = index.get(key)
    if not row:
        return None

    if key == row["id"]:
        return row["name"]
    if key == row["name"]:
        return row["email"]
    if key == row["email"]:
        return row["id"]

print(lookup(1))
#Returns name
 
print(lookup("Javagner da Silva"))
#Returns email

print(lookup("rusthon@cafecomvenvanse.com"))
#Returns id