#!/usr/bin/python3
"""This script uses a REST API, given an employee ID, returns
information about his/her TODO list progress."""


if __name__ == "__main__":
    import requests
    from sys import argv

    id = int(argv[1])
    index = id - 1
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        id)
    user_url = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(todo_url).json()
    u = requests.get(user_url)
    employee_name = u.json()[index].get('name')

    total = 0
    completed = 0
    task_completed = []
    for i in r:
        total += 1
        if i.get('completed') is True:
            completed += 1
            task_completed.append(i.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed, total))
    for task in task_completed:
        print("\t {}".format(task))
