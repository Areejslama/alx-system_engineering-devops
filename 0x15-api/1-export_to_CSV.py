#!/usr/bin/python3
"""this script to gather data"""
import requests
import sys
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()
    complete = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(complete), len(todos)))
    [print("\t {}".format(i)) for i in complete]
    with open ("{}.csv".format(employee_id), "w")as f:
        write = csv.writer(f)
        write.writerow(['USER_ID', 'USERNAME', 
            'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for t in todos:
            write.writerow([employee_id, employee.get("username"),
                t.get("completed"), t.get("title")])
