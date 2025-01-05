from cs50 import get_int

def main():
    meow()

def meow():
    n = get_int("Input an int: ")
    for i in range(n):
        print("#")
main()