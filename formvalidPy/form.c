#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to check if a string is a valid email
int isValidEmail(const char *email) {
    int atSymbol = 0;
    int dotSymbol = 0;
    while (*email) {
        if (*email == '@') {
            atSymbol++;
        } else if (*email == '.') {
            dotSymbol++;
        }
        email++;
    }
    return (atSymbol == 1 && dotSymbol > 0);
}

int main() {
    char email[100];
    printf("Enter your email: ");
    scanf("%99s", email);

    if (isValidEmail(email)) {
        printf("Valid email.\n");
    } else {
        printf("Invalid email.\n");
    }

    return 0;
}