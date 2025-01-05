import csv
from cs50 import get_string, get_int

# Open the file in append mode to add new entries without overwriting
with open("phone.csv", "a", newline="") as file:
    # Prompt the user for input
    name = get_string("Name: ")
    number = get_string("Number: ")

    # Create a CSV writer object
    writer = csv.writer(file)

    # Write a new row to the file
    writer.writerow([name, number])

print("Entry saved successfully.")
