#include <iostream>
#include <regex>

// Function to check if a string is a valid email using regex
bool isValidEmail(const std::string &email)
{
    const std::regex pattern(R"((\w+)(\.{0,1})(\w*)@(\w+)\.(\w+))");
    return std::regex_match(email, pattern);
}

int main()
{
    std::string email;
    std::cout << "Enter your email: ";
    std::cin >> email;

    if (isValidEmail(email))
    {
        std::cout << "Valid email." << std::endl;
    }
    else
    {
        std::cout << "Invalid email." << std::endl;
    }

    return 0;
}