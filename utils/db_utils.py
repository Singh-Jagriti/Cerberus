# C:\Users\singh\PycharmProjects\Cerberus\utils\db_utils.py

import sqlite3
import logging

class DBUtils:
    def __init__(self, db_name='test_database.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self._connect()

    def _connect(self):
        """Establishes a connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self.logger.info(f"Connected to database: {self.db_name}")
        except sqlite3.Error as e:
            self.logger.error(f"Error connecting to database {self.db_name}: {e}")
            raise

    def close_connection(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()
            self.logger.info(f"Database connection to {self.db_name} closed.")

    def execute_query(self, query, params=()):
        """Executes a generic SQL query."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            self.logger.debug(f"Executed query: {query} with params: {params}")
            return self.cursor
        except sqlite3.Error as e:
            self.logger.error(f"Error executing query '{query}' with params {params}: {e}")
            self.conn.rollback() # Rollback changes on error
            raise

    def fetch_one(self, query, params=()):
        """Executes a query and fetches one row."""
        cursor = self.execute_query(query, params)
        return cursor.fetchone()

    def fetch_all(self, query, params=()):
        """Executes a query and fetches all rows."""
        cursor = self.execute_query(query, params)
        return cursor.fetchall()

    def create_users_table(self):
        """Ensures the 'users' table exists and adds dummy data."""
        self.logger.info("Ensured 'users' table exists.")
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT,
            full_name TEXT
        );
        """
        self.execute_query(create_table_query)

        self.logger.info("Attempting to add dummy data to 'users' table.")
        # Add dummy data only if it doesn't already exist
        dummy_data_query = """
        INSERT OR IGNORE INTO users (id, username, email, full_name) VALUES (?, ?, ?, ?);
        """
        # Using INSERT OR IGNORE will prevent errors if data already exists
        self.execute_query(dummy_data_query, (1, 'jsingh', 'jagriti@example.com', 'Jagriti Singh'))
        self.execute_query(dummy_data_query, (2, 'johndoe', 'john.doe@example.com', 'John Doe'))
        self.logger.info("Dummy data added/ensured in 'users' table.")

    def get_user_by_id(self, user_id):
        """Public method to get a user by their ID."""
        self.logger.info(f"Fetching user by ID: {user_id}")
        query = "SELECT id, username, email, full_name FROM users WHERE id = ?;"
        return self.fetch_one(query, (user_id,))

    # Example of another public method if needed
    def public_method_example(self):
        self.logger.info("Public method create_users_table called.")
        self.create_users_table() # This can be called from outside the class