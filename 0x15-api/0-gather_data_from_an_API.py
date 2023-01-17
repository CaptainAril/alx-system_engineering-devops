#!/usr/bin/python3
"""Returns infomation on an employees TODO progress."""

if __name__ == "__main__":
    import requests
    from sys import argv

    id = argv[1]
    user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    u = requests.get(user).json()
    employee = u.get("name")
    task_done = 0

    todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    r = requests.get(todo).json()
    total_task = len(r)

    complete_task = []
    for todo in r:
        # print(todo)
        if todo.get("completed") is True:
            task_done += 1
            complete_task.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        employee, task_done, total_task))
    for task in complete_task:
        print("\t {}".format(task))
