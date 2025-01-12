#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>
#include <iostream>

void connectToMySQL() {
    const std::string server = "tcp://127.0.0.1:3306"; // Replace with your MySQL server
    const std::string username = "your_username";      // Replace with your MySQL username
    const std::string password = "your_password";      // Replace with your MySQL password
    const std::string database = "your_database";      // Replace with your database name

    try {
        // Create a MySQL driver instance
        sql::Driver *driver = get_driver_instance();

        // Create a connection
        std::unique_ptr<sql::Connection> connection(driver->connect(server, username, password));

        std::cout << "Connected to MySQL server successfully!" << std::endl;

        // Select the database
        connection->setSchema(database);

        // Create a statement object
        std::unique_ptr<sql::Statement> statement(connection->createStatement());

        // Execute a query
        std::unique_ptr<sql::ResultSet> result(statement->executeQuery("SELECT DATABASE();"));

        // Process the results
        if (result->next()) {
            std::cout << "Connected to database: " << result->getString(1) << std::endl;
        }
    } catch (sql::SQLException &e) {
        std::cerr << "SQLException: " << e.what() << std::endl;
        std::cerr << "Error code: " << e.getErrorCode() << std::endl;
        std::cerr << "SQLState: " << e.getSQLState() << std::endl;
    }
}

int main() {
    connectToMySQL();
    return 0;
}
