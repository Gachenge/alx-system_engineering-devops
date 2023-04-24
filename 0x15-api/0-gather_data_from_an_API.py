#!/usr/bin/python3
"""extend 0-gather data to export data in json
export all tasks from all employees"""

import requests
from sys import argv

user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                    .format(argv[1])).json()
tasks = requests.get("https://jsonplaceholder.typicode.com/todos",
                     params={"userId": argv[1]}).json()

tak = []
for task in tasks:
    if task.get("completed") is True:
        tak.append(task.get("title"))

print("Employee {} is done with tasks({}/{}):"
      .format(user.get("name"), len(tak), len(tasks)))
for ta in tak:
    print("\t", ta)
