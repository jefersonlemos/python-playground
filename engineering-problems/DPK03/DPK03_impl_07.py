'''
Approach: Define and Write down the approach
'''

data_map = [
    {"id": 1, "name": "Kuberneide Arantes", "email": "kuberneto@aol.com"},
    {"id": 2, "name": "Javagner da Silva", "email": "javagner@bol.com"},
    {"id": 3, "name": "Rustina Souza Python", "email": "rusthon@cafecomvenvanse.com"}
]

# results = [
#     {"id":"name"},
#     {"name":"email"},
#     {"email":"id"}
# ]
results = {
    "id":"name",
    "name":"email",
    "email":"id"
}

# def lookup(key):
#     for result_item in results:
#         print(result_item)

def lookup(key):
    for result_item in results:
        for data_item in data_map:
            if data_item[result_item] == key:
                return data_item[results[result_item]]

print(lookup(1))
#Returns name
 
print(lookup("Javagner da Silva"))
#Returns email

print(lookup("rusthon@cafecomvenvanse.com"))
#Returns id