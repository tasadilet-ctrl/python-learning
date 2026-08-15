class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
class Course:
    def __init__(self, student, max_students):
        self.student = student
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students)
        

s1 = Student("Tim", 20, 95)
s2 = Student("Bill", 22, 75)
s3 = Student("Jill", 21, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)  # Output: Tim
print(course.students[1].name)  # Output: Bill
print(course.get_average_grade())  # Output: 85.0