import csv

houses = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}

with open ("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) #ignores the 1st line
    
    for row in reader:
        house = row[1]
        houses[house] +=1
        
for house in houses:
    count = houses[house]
    print(f"{house}: {count}")