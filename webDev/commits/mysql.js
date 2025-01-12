const mysql = require('mysql2');

function connectToMySQL() {
  // Create a connection to the database
  const connection = mysql.createConnection({
    host: 'localhost',       // Replace with your MySQL server hostname or IP
    user: 'your_username',   // Replace with your MySQL username
    password: 'your_password', // Replace with your MySQL password
    database: 'your_database'  // Replace with your database name
  });

  // Connect to the database
  connection.connect((err) => {
    if (err) {
      console.error('Error connecting to MySQL:', err.message);
      return;
    }
    console.log('Connected to MySQL database!');
  });

  // Perform a query
  connection.query('SELECT DATABASE();', (err, results) => {
    if (err) {
      console.error('Error executing query:', err.message);
    } else {
      console.log('Connected to database:', results[0]['DATABASE()']);
    }

    // Close the connection
    connection.end((err) => {
      if (err) {
        console.error('Error closing the connection:', err.message);
      } else {
        console.log('MySQL connection closed.');
      }
    });
  });
}

// Call the function
connectToMySQL();
