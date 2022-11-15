#!/usr/bin/python3
"""Extends the `gather_data_from_an_API` script; and exports data in
CSV format.
"""


if __name__ == "__main__":
    import csv
    import json
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

    with open('{}.json'.format(id), 'w') as file:
        usr = {id: []}
        for task in r:
            task_title = task.get('title')
            task_stats = task.get('completed')
            usr_dict = {"task": task_title,
                        "comleted": task_stats,
                        "username": employee_username}
            usr.get(id).append(usr_dict)

        json.dump(usr, file)
