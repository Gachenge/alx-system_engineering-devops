#!/usr/bin/python3
"""export files from an API format it by user id
export formated data into CSV"""

from sys import argv
import csv
import requests

user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                    .format(argv[1])).json()
tasks = requests.get("https://jsonplaceholder.typicode.com/todos",
                     params={"userId": argv[1]}).json()

USER_ID = argv[1]
USERNAME = user.get("username")
with open("{}.csv".format(USER_ID), 'w', encoding='utf8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    [writer.writerow
     ([USER_ID, USERNAME, task.get("completed"), task.get("title")])
     for task in tasks]
