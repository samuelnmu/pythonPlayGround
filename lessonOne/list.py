from cs50 import get_int
from cs50 import get_string

print("Welcome To our phonebook Manager")
name = get_string("Input name: ")
print(f"Hello {name}")
number = get_int("Input Phone number: ")

phonebook = {
    name : number
}

print(phonebook)