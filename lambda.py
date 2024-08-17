people = [
    {"name":"Harry","house":"Gryffindor"},
    {"name":"cho","house":"Revenclaw"},
    {"name":"Draco","house":"Slytherin"}
]

def f(person):
    return person["house"]

people.sort(key=lambda person: person["name"])

print(people)
