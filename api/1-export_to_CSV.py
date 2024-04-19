#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


def EXPORT_TO_CSV(ID):
    """
    This function gets the date from jsonplaceholder.typicode.com
    and savzes it in a csv file
    """
    # gather a specific data by the ID
    data = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    ).json()
    user = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{ID}"
    ).json()

    with open(f"{ID}.csv", mode="w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in data:
            writer.writerow(
                [
                    (ID),
                    user["username"],
                    todo["completed"],
                    todo["title"],
                ]
            )


if __name__ == "__main__":
    ID = sys.argv[1]

    EXPORT_TO_CSV(ID)
