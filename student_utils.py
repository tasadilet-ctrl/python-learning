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