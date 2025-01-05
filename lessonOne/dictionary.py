from cs50 import get_string

people = {
    "Samuel" : "0713625483",
    "Ngige" : "samuelnmu",
    "Machine" : "Benz GLC"
}

name = get_string("Enter Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")
    