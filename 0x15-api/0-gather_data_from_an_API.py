#!/usr/bin/python3
"""this script to gather data"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"user_Id": employee_id}).json()
    complete = [todo.get("title")for todo in todos if todo.get("complete") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(complete), len(todos)))
    [print("\t {}".format(t) for t in complete)]
