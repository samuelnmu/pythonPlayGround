import re

def is_valid_email(email):
    # Regular expression for validating an Email
    pattern = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(pattern, email)

email = input("Enter your email: ")
if is_valid_email(email):
    print("Valid email.")
else:
    print("Invalid email.")