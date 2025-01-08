people = [
    {"name":"Harry", "House":"Griffyndor"},
    {"name":"Samuel", "House":"Ravenclaw"},
    {"name":"john", "House":"slytherin"}
]

def f(person):
    return person("name")

#lambda function
people.sort(key= lambda person : person["name"])

people.sort(key=f)

print(people)