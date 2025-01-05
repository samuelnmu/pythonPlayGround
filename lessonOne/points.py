from cs50 import get_int
from cs50 import get_string

print("Welcome to our points grader!")
user = get_string("What is your name? ") 
welcome = print(f"Hello, {user}")
points = get_int("How many points did you loose? ")

if points < 4:
    print(f"{user}, You lost fewer points than me.")
elif points > 4:
    print(f"{user}, You lost more points than me!")
elif points == 4:
    print(f"{user}, We lost same points")
else:
    print(f"{user}, Invalid input! ")