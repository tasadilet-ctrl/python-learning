# # # def greet(name):
# # #     print(f"Hello, {name}!")

# # # greet("Tom Smith")

# # def is_even(n):
# #     if n % 2 == 0:
# #         return True
# #     else:
# #         return False

# # if is_even(5):
# #     print("5 is even.")
# # else:
# #     print("5 is odd.")

# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#         return None

# def get_number(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# print(
#     safe_divide(
#         get_number("Enter number 1: "),
#         get_number("Enter number 2: ")
#     )
# )

# student1 = {"name": "Alice", "age": 30, "courses": ["Math", "Science"]}
# student2 = {"name": "Bob", "age": 25, "courses": ["English", "History"]}
# student3 = {"name": "Charlie", "age": 17, "courses": ["Math", "Art"]}


# def add_course(student, course):
#     student["courses"].append(course)


# def is_adult(student):
#     if student["age"] >= 18:
#         return True
#     else:
#         return False


# unique_courses = set()
# for student in [student1, student2, student3]:
#     unique_courses.update(student["courses"])
# print(f"Unique courses: {unique_courses}")

# students = [
#     {"name": "Alice", "age": 30, "courses": ["Math", "Science"]},
#     {"name": "Bob", "age": 25, "courses": ["English", "History"]},
#     {"name": "Charlie", "age": 17, "courses": ["Math", "Art"]},
# ]

# def student_in_course(students, course):
#     names = []
#     for student in students:
#         if course in student["courses"]:
#             names.append(student["name"])
#     return names
# print(student_in_course(students, "Math"))  # ['Alice', 'Charlie']

# def average_age(students):
#     total_age = 0
#     for student in students:
#         total_age += student["age"]
#     return total_age / len(students)
# print(average_age(students))  # 24.0

students = [
    {"name": "Alice", "age": 30, "courses": ["Math", "Science"]},
    {"name": "Bob", "age": 25, "courses": ["English", "History"]},
    {"name": "Charlie", "age": 17, "courses": ["Math", "Art"]},
]

def courses_by_student(students_examples):
    names_and_courses = {}
    for student in students_examples:
        names_and_courses[student["name"]] = student["courses"]
    return names_and_courses

print(courses_by_student(students))
