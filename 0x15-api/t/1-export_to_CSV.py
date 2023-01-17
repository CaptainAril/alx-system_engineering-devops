#!/usr/bin/python3
"""Extends the `gather_data_from_an_API` script; and exports data in
CSV format.
"""


if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    id = int(argv[1])
    index = id - 1
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        id)
    user_url = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(todo_url).json()
    u = requests.get(user_url)
    employee_username = u.json()[index].get('username')

    with open("{}.csv".format(id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in r:
            task_title = task.get('title')
            task_status = task.get('completed')
            writer.writerow([id, employee_username, task_status, task_title])
