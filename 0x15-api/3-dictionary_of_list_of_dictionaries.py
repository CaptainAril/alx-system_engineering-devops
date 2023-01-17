#!/usr/bin/python3
"""Returns infomation on all users task status,
and esports to JSON format."""

if __name__ == "__main__":
    import csv
    import json
    import requests

    user = "https://jsonplaceholder.typicode.com/users"
    u = requests.get(user).json()
    all_employees = {}
    for user in u:
        id = user.get('id')
        username = user.get('username')
        all_employees[id] = []

        todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        r = requests.get(todo).json()

        for task in r:
            title = task.get('title')
            status = task.get('completed')
            tk = {'username': username, "task": title, 'completed': status}
            all_employees[id].append(tk)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_employees, f)
