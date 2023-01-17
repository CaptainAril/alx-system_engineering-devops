#!/usr/bin/python3
"""Returns infomation on user's task status,
and esports to CSV format."""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    id = argv[1]
    user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    u = requests.get(user).json()
    username = u.get("username")

    todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    r = requests.get(todo).json()
    with open("{}.csv".format(id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in r:
            task_title = task.get('title')
            task_status = task.get('completed')
            writer.writerow([id, username, task_status, task_title])
