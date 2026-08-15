# #Open file as writing
# with open("day3.txt", "w") as file:
#     file.write("This is the first line.\n")
#     file.write("This is the second line.\n")

# with open("day3.txt", "r") as file:
#     lines = file.readlines()

# print(lines)

students = [
    {"name": "Alice", "age": 30, "courses": ["Math", "Science"]},
    {"name": "Bob", "age": 25, "courses": ["English", "History"]},
    {"name": "Charlie", "age": 17, "courses": ["Math", "Art"]},
]

def write_students_to_file(students_examples, filename):
    try:
        with open(filename, "w") as file:
            for student in students_examples:
                line = f"{student['name']} : {' , '.join(student['courses'])}\n"
                file.write(line)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except PermissionError:
        print(f"Permission denied while writing to file {filename}.")


write_students_to_file(students, "students.txt")

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

read_students = read_students_from_file("students.txt")
print(read_students)