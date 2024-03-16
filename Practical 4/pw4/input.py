from pw4.domains.student import Student
from pw4.domains.course import Course
from pw4.domains.marks_sheet import MarksSheet

import random

def manual_input(sms):
    stu_num = int(input("Enter number of students in class: "))
    for i in range(stu_num):
        student = Student(input("Enter student ID: "), input("Enter student name: "), input("Enter student DoB: "))
        sms.students.append(student)

    course_num = int(input("Enter number of courses: "))
    for i in range(course_num):
        course = Course(input("Enter course ID: "), input("Enter course name: "), int(input("Enter course credit: ")))
        sms.courses.append(course)

def lazy_input(sms):
    stu_num = random.randint(5, 10)
    print(f"Enter number of students in class: {stu_num}")
    stu_names = ["Alex", "Ben", "Charlie", "Dan", "Frank"]
    for i in range(stu_num):
        student = Student(i+1, random.choice(stu_names), f"{random.randint(1, 31)}/{random.randint(1, 12)}")
        sms.students.append(student)

    course_num = random.randint(3, 5)
    print(f"Enter number of courses: {course_num}")
    course_names = ["Math", "Physic", "Chemistry", "Bio", "Programming"]
    for i in range(course_num):
        course = Course(i+1, course_names[i], random.randint(1, 3))
        sms.courses.append(course)

    for course in sms.courses:
        marks_sheet = MarksSheet()
        for student in sms.students:
            mark = random.randint(0, 20)
            marks_sheet.add_mark(student.ID, mark)
            student.set_marks(course.ID, mark)
        sms.marks_sheets.append(marks_sheet)
