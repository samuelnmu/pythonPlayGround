#include <iostream>
#include <map>
#include <string>

std::map<std::string, bool> logged_in_users = {
    {"samuelnmu", true},
    {"janedoe", false},
    {"johndoe", true}
};

bool is_user_logged_in(const std::string &username) {
    auto it = logged_in_users.find(username);
    if (it != logged_in_users.end()) {
        return it->second;
    }
    return false; // User not found or not logged in
}

int main() {
    std::string username_to_check = "samuelnmu";
    if (is_user_logged_in(username_to_check)) {
        std::cout << "The user '" << username_to_check << "' is logged in." << std::endl;
    } else {
        std::cout << "The user '" << username_to_check << "' is not logged in." << std::endl;
    }
    return 0;
}