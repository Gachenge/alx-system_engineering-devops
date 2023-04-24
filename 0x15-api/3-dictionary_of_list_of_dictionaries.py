#!/usr/bin/python3
"""extend 0-gather data to export data in json
export all tasks from all employees"""

from sys import argv
import requests
import json

users = requests.get("https://jsonplaceholder.typicode.com/users").json()
tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()

user = {user.get("id"): [{"username": user.get("username"), "task":
                          task.get("title"), "completed":
                          task.get("completed")}
        for task in requests.get
        ("https://jsonplaceholder.typicode.com/todos",
            params={"userId": user.get("id")}).json()]
        for user in users}
usson = json.dumps(user, sort_keys=True)

with open('todo_all_employees.json', 'w') as f:
    f.write(usson)
