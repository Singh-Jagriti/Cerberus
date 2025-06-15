# Directory: behave_cerberus/utils/db_utils.py
import sqlite3

class DBUtils:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def fetch_user_by_id(self, user_id):
        self.cursor.execute("SELECT name FROM users WHERE id=?", (user_id,))
        row = self.cursor.fetchone()
        return row[0] if row else None

    def close(self):
        self.conn.close()