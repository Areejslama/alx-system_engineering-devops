#!/usr/bin/python3
"""this script to gather data"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()
    complete = [t.get("title") for t in todos if t.get("completed") is True]
    with open("{}.csv".format(employee_id), "w")as f:
        write = csv.writer(f,  quoting=csv.QUOTE_ALL)
    for t in todos:
        write.writerow(
                [employee_id, employee.get("username"),
                    t.get("completed"), t.get("title")])
