#!/usr/bin/python3
"""Extends the `gather_data_from_an_API` script; and exports data in
CSV format.
"""


if __name__ == "__main__":
    import json
    import requests

    user_url = 'https://jsonplaceholder.typicode.com/users'
    u = requests.get(user_url).json()

    with open('todo_all_employees.json', 'w') as file:
        all_employees = {}
        for user in u:
            id = user.get('id')
            usrname = user.get('username')

            todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
                .format(id)
            r = requests.get(todo_url).json()
            usr_dict = []
            for task in r:
                task_title = task.get('title')
                task_stats = task.get('completed')
                usr_task = {"username": usrname,
                            "task": task_title,
                            "completed": task_stats}
                usr_dict.append(usr_task)

            all_employees[id] = usr_dict

        json.dump(all_employees, file)
