#include <mysql/mysql.h>
#include <stdio.h>
#include <stdlib.h>

void connect_to_mysql()
{
    // MySQL connection variables
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    const char *server = "localhost";       // Replace with your MySQL server hostname or IP
    const char *user = "your_username";     // Replace with your MySQL username
    const char *password = "your_password"; // Replace with your MySQL password
    const char *database = "your_database"; // Replace with your database name

    // Initialize connection
    conn = mysql_init(NULL);
    if (conn == NULL)
    {
        fprintf(stderr, "mysql_init() failed\n");
        exit(EXIT_FAILURE);
    }

    // Connect to the database
    if (mysql_real_connect(conn, server, user, password, database, 0, NULL, 0) == NULL)
    {
        fprintf(stderr, "mysql_real_connect() failed\n");
        fprintf(stderr, "Error: %s\n", mysql_error(conn));
        mysql_close(conn);
        exit(EXIT_FAILURE);
    }

    printf("Connected to MySQL database successfully!\n");

    // Execute a query
    if (mysql_query(conn, "SELECT DATABASE();"))
    {
        fprintf(stderr, "Query failed: %s\n", mysql_error(conn));
        mysql_close(conn);
        exit(EXIT_FAILURE);
    }

    // Retrieve the result set
    res = mysql_store_result(conn);
    if (res == NULL)
    {
        fprintf(stderr, "mysql_store_result() failed: %s\n", mysql_error(conn));
        mysql_close(conn);
        exit(EXIT_FAILURE);
    }

    // Print the result
    while ((row = mysql_fetch_row(res)) != NULL)
    {
        printf("Connected to database: %s\n", row[0]);
    }

    // Clean up
    mysql_free_result(res);
    mysql_close(conn);
    printf("MySQL connection closed.\n");
}

int main()
{
    connect_to_mysql();
    return 0;
}
