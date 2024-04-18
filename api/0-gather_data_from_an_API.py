#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def TODO_REQUESTS(ID):
    """
    This function gets the date from jsonplaceholder.typicode.com
    and shows it
    """
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    ).json()
    user = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{ID}"
    ).json()
    completed_tasks = [task["title"] for task in todos if task["completed"]]
    print(
        f"Employee {user['name']} is done with tasks\
({len(completed_tasks)}/{len(todos)}):"
    )
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    ID = sys.argv[1]

    TODO_REQUESTS(ID)
