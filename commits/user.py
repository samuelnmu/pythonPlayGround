# Dictionary to simulate logged-in users (usernames as keys)
logged_in_users = {
    'samuelnmu': True,
    'janedoe': False,
    'johndoe': True
}

def is_user_logged_in(username):
    """
    Check if a user is logged in.

    Parameters:
    username (str): The username to check

    Returns:
    bool: True if the user is logged in, False otherwise
    """
    return logged_in_users.get(username, False)

# Example usage
username_to_check = 'samuelnmu'
if is_user_logged_in(username_to_check):
    print(f"The user '{username_to_check}' is logged in.")
else:
    print(f"The user '{username_to_check}' is not logged in.")