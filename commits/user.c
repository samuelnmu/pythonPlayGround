#include <stdio.h>
#include <string.h>

#define USERS_COUNT 3

typedef struct
{
    char username[50];
    int is_logged_in;
} User;

User users[USERS_COUNT] = {
    {"samuelnmu", 1},
    {"janedoe", 0},
    {"johndoe", 1}};

int is_user_logged_in(const char *username)
{
    for (int i = 0; i < USERS_COUNT; i++)
    {
        if (strcmp(users[i].username, username) == 0)
        {
            return users[i].is_logged_in;
        }
    }
    return 0; // User not found or not logged in
}

int main()
{
    const char *username_to_check = "samuelnmu";
    if (is_user_logged_in(username_to_check))
    {
        printf("The user '%s' is logged in.\n", username_to_check);
    }
    else
    {
        printf("The user '%s' is not logged in.\n", username_to_check);
    }
    return 0;
}