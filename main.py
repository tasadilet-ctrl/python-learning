# students = [
#     {"name": "Alice", "age": 30, "courses": ["Math", "Science"]},
#     {"name": "Bob", "age": 25, "courses": ["English", "History"]},
#     {"name": "Charlie", "age": 17, "courses": ["Math", "Art"]},
# ]

# import student_utils
# student_utils.write_students_to_file(students, "students.txt")
# read_students = student_utils.read_students_from_file("students.txt")
# print(read_students)

# import math
# import random
# print(math.sqrt(16))
# print(random.randint(1, 10))

import os

# Create the 'students' directory if it doesn't exist
os.makedirs('students', exist_ok=True)

# The content you want to write to io.py
io_content = '''
def write_students_to_file(students, filename):
    try:
        with open(filename, "w") as file:
            for student in students:
                line = f"{student['name']} : {' , '.join(student['courses'])}\n"
                file.write(line)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except PermissionError:
        print(f"Permission denied while writing to file {filename}.")

def read_students_from_file(filename):
    try:
        with open(filename, "r") as file:
            new_students = []
            lines = file.readlines()
            for line in lines:
                name, courses_str = line.strip().split(" : ")
                courses = courses_str.split(" , ")
                new_students.append({"name": name, "courses": courses})
            return new_students
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except ValueError:
        print(f"File {filename} has formatting errors.")
        return []
'''

# Write the content to io.py
with open('students/io.py', 'w') as file:
    file.write(io_content)

stats_content = '''
def average_age(students):
    total_age = sum(student['age'] for student in students)
    return total_age / len(students)
'''

# Write the content to stats.py
with open('students/stats.py', 'w') as file:
    file.write(stats_content)

from students.io import read_students_from_file, write_students_to_file
from students.stats import average_age

students = [
    {"name": "Alice", "age": 30, "courses": ["Math", "Science"]},
    {"name": "Bob", "age": 25, "courses": ["English", "History"]},
    {"name": "Charlie", "age": 17, "courses": ["Math", "Art"]},
]

write_students_to_file(students, "students.txt")
read_students = read_students_from_file("students.txt")

print(f"Average age: {average_age(read_students)}")