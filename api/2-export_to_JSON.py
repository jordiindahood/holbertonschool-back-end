#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


def EXPORT_TO_JSON(ID):
    """
    This function gets the date from jsonplaceholder.typicode.com
    and savzes it in a json file
    """
    # gather a specific data by the ID
    data = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    ).json()
    user = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{ID}"
    ).json()

    # data format:
    formatted_data = {
        ID: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user["username"],
            }
            for task in data
        ]
    }
    json_object = json.dumps(formatted_data)
    
    #saving data in JSON file
    with open(f"{ID}.json", mode="w") as json_file:
        json_file.write(json_object)


if __name__ == "__main__":
    ID = sys.argv[1]

    EXPORT_TO_JSON(ID)
