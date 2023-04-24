#!/usr/bin/python3
"""extend 0-gather to export the data to JSON format record all tasks owned by this employee"""

from sys import argv
import requests
import json

user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                    .format(argv[1])).json()
tasks = requests.get("https://jsonplaceholder.typicode.com/todos",
                     params={"userId": argv[1]}).json()

use = {argv[1]: [{"task": task.get("title"), "completed":
                  task.get("completed"), "username": user.get("username")}
                 for task in tasks]}
usson = json.dumps(use)

with open("{}.json".format(argv[1]), "w") as f:
    f.write(usson)
