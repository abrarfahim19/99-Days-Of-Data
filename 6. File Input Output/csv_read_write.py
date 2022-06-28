import csv

students = []


############### Using CSV reader ####################
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name,home in reader:
#         student = {"name":name, "home":home}
#         students.append(student)
#
# for student in sorted(students, key=lambda student:student['name']):
#     print(student)


############### Using DictReader ####################
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append(row)

# for student in sorted(students, key=lambda student:student['Name']):
#     print(student)

############## Writing CSV ##########################
one_more = 1
with open("student_written.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["Name", "Home"])
    writer.writeheader()
    while (int(one_more) == 1):
        writer.writerow({"Name":input("Name = ? \n"),"Home":input("Home = ?\n")})
        one_more = input("Press 1 for Input\n")