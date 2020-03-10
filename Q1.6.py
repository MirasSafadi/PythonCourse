comp = {
    "accounting": [
        {"firstName": "John", "lastName": "Doe", "age": 23},
        {"firstName": "Mary", "lastName": "Smith", "age": 32}
    ],
    "sales": [
        {"firstName": "Sally", "lastName": "Green", "age": 27},
        {"firstName": "Jim", "lastName": "Galley", "age": 41}
    ]
}
minAge = 10000
for L in comp.values():
    for dic in L:
        if(dic.get("age")<minAge):
            minAge = dic.get("age")
print(minAge)
comp["sales"].append({"firstName": "Rima", "lastName": "Moon", "age": 21})
print(comp["sales"])

dept = str(input("Enter department name.."))
name = str(input("Enter worker name.."))
if(comp.get(dept) != None):
    L = comp.get(dept)
    #search for name in L
    for dic in L:
        if(dic.get("firstName") == name):
            L.remove(dic)
            break
    # print("No such person!")
else:
    print("No such department")
print(comp)