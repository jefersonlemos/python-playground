'''
Approach: Define and Write down the approach
'''

data_map = [
    {"id": 1, "name": "Kuberneide Arantes", "email": "kuberneto@aol.com"},
    {"id": 2, "name": "Javagner da Silva", "email": "javagner@bol.com"},
    {"id": 3, "name": "Rustina Souza Python", "email": "rusthon@cafecomvenvanse.com"}
]

def lookup(key):
    fields = ["id", "name", "email"]
    
    for record in data_map:
        for i in range(len(fields)):
            if record[fields[i]] == key:
                next_i = (i + 1) % len(fields)
                return record[fields[next_i]]
    
    return None

print(lookup(1))
# Returns name
 
print(lookup("Javagner da Silva"))
# Returns email

print(lookup("rusthon@cafecomvenvanse.com"))
# Returns id
