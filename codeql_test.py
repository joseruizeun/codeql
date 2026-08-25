# codeql_test.py
# Intentionally vulnerable code for testing CodeQL security scanning setup.
# Do NOT use these patterns in real code.

import os
import sqlite3


def run_command(user_input):
    # Command injection (CWE-78)
    os.system("echo " + user_input)


def get_user(db_path, username):
    # SQL injection (CWE-89)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    run_command("test")
