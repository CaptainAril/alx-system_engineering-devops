#!/usr/bin/python3
"""Returns infomation on user's task status,
and esports to JSON format."""

if __name__ == "__main__":
    import csv
    import json
    import requests
    from sys import argv

    id = argv[1]
    user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    u = requests.get(user).json()
    username = u.get("username")

    todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    r = requests.get(todo).json()

    user_status = {}
    user_status[id] = []
    print(user_status)
    for task in r:
        title = task.get('title')
        status = task.get('completed')
        tk = {"task": title, 'completed': status, 'username': username}
        user_status[id].append(tk)
    print(user_status)
    with open('{}.json'.format(id), 'w') as f:
        json.dump(user_status, f)
