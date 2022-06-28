import csv

with open('some_text.txt') as file:
    lines = file.readlines()
    for row in lines:
        print(row.rstrip())
