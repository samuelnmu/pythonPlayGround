from cs50 import get_string

user = get_string("Input username: ")
print(f"Hello, {user}")
policy = get_string("Do you agree? Y/N: ")

if policy == "Y" or policy == "y":
    print("Agreed.")
elif policy == "N" or policy == "n":
    print("Not agreed!")
else:
    print("Input correct value!")