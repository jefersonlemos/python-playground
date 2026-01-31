'''
Approach: Iterate through keys within each dictionary to find matching value. It uses the modulo (divider)
operator to define the index
'''

data_map = [
    {"id": 1, "name": "Kuberneide Arantes", "email": "kuberneto@aol.com"},
    {"id": 2, "name": "Javagner da Silva", "email": "javagner@bol.com"},
    {"id": 3, "name": "Rustina Souza Python", "email": "rusthon@cafecomvenvanse.com"}
]

def lookup(key):
    for item in data_map:
        keys = ["id", "name", "email"]
        for i in range(len(keys)):
            if item[keys[i]] == key:
                next_index = (i + 1) % len(keys)
                return item[keys[next_index]]
    return None

print(lookup(1))
print(lookup("Javagner da Silva"))
print(lookup("rusthon@cafecomvenvanse.com"))
