const loggedInUsers = {
    'samuelnmu': true,
    'janedoe': false,
    'johndoe': true
};

function isUserLoggedIn(username) {
    return loggedInUsers[username] || false;
}

// Example usage
const usernameToCheck = 'samuelnmu';
if (isUserLoggedIn(usernameToCheck)) {
    console.log(`The user '${usernameToCheck}' is logged in.`);
} else {
    console.log(`The user '${usernameToCheck}' is not logged in.`);
}