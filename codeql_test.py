import os
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)

# NOTE: Not a real credential.
GITHUB_TOKEN = "ghp_0000000000000000000000000000000000"


@app.route("/run")
def run_command():
    user_input = request.args.get("cmd", "")

    # Fixed: avoid shell command construction from user input.
    subprocess.run(["echo", user_input], check=False)

    return "done"


@app.route("/user")
def get_user():
    db_path = "users.db"
    username = request.args.get("username", "")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Use parameterized query to avoid SQL injection from user-controlled input.
    cursor.execute("SELECT * FROM users WHERE name = ?", (username,))

    return str(cursor.fetchall())


if __name__ == "__main__":
    app.run()
