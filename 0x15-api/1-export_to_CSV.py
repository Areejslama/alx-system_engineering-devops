#!/usr/bin/python3
"""this script to export data to csv format"""
import csv


with open ("USER_ID.csv", "w")as f:
    write = csv.writer(f)
    write.writerow(['USER_ID', 'USERNAME'])
    write.writerow(['TASK_COMPLETED_STATUS', 'TASK_TITLE'])
