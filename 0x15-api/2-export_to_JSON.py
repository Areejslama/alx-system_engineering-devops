#!/usr/bin/python3
"""this script to gather data"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()
    complete = [t.get("title") for t in todos if t.get("completed") is True]
    with open("{}.json".format(employee_id), "w") as f:
        json.dump({
            employee_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": employee.get("username")
            } for t in todos]
        }, f)
