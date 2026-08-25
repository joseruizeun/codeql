import os
import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/run")
def run_command():
    user_input = request.args.get("cmd", "")

    # Command injection
    os.system("echo " + user_input)

    return "done"


@app.route("/user")
def get_user():
    db_path = "users.db"
    username = request.args.get("username", "")

    # SQL injection
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE name = '" + username + "'"

    cursor.execute(query)

    return str(cursor.fetchall())


if __name__ == "__main__":
    app.run()
