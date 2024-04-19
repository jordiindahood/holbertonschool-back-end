#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests


def EXPORT_ALL_USERS_TO_JSON():
    """
    This function gets all users data from jsonplaceholder.typicode.com
    and saves it in a json file
    """
    # gather a specific data by the ID
    data = requests.get(f"https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users"
    ).json()

    # data format:
    formatted_data = {
        user["id"]: [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in data
            if task["userId"] == user["id"]
        ]
        for user in users
    }
    json_object = json.dumps(formatted_data)

    # saving data in JSON file
    with open("todo_all_employees.json", mode="w") as json_file:
        json_file.write(json_object)


if __name__ == "__main__":
    EXPORT_ALL_USERS_TO_JSON()
