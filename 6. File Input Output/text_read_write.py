import csv

with open('students.csv') as file:
    lines = csv.DictReader(file)
    for row in lines:
        print(row)
