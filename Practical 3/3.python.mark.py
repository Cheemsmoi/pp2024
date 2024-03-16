import random
import math
import numpy as np

class Student:
    def __init__(self, ID, name, dob):
        self.ID = ID
        self.name = name
        self.dob = dob
        self.marks = {}

    def set_marks(self, course_id, mark):
        self.marks[course_id] = mark

    def get_marks(self, course_id):
        return self.marks.get(course_id, None)

    def calculate_gpa(self, courses):
        total_weighted_sum = 0
        total_credits = 0
        for course_id, mark in self.marks.items():
            course = next((course for course in courses if course.ID == course_id), None)
            if course:
                total_weighted_sum += mark * course.credit
                total_credits += course.credit
        if total_credits == 0:
            return 0
        return total_weighted_sum / total_credits

class Course:
    def __init__(self, ID, name, credit):
        self.ID = ID
        self.name = name
        self.credit = credit

class MarksSheet:
    def __init__(self):
        self.marks = {}

    def add_mark(self, student_id, mark):
        self.marks[student_id] = mark

    def get_mark(self, student_id):
        return self.marks.get(student_id, None)

class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks_sheets = []

    def manual_input(self):
        stu_num = int(input("Enter number of students in class: "))
        for i in range(stu_num):
            student = Student(input("Enter student ID: "), input("Enter student name: "), input("Enter student DoB: "))
            self.students.append(student)

        course_num = int(input("Enter number of courses: "))
        for i in range(course_num):
            course = Course(input("Enter course ID: "), input("Enter course name: "), int(input("Enter course credit: ")))
            self.courses.append(course)

    def lazy_input(self):
        stu_num = random.randint(5, 10)
        print(f"Enter number of students in class: {stu_num}")
        stu_names = ["Alex", "Ben", "Charlie", "Dan", "Frank"]
        for i in range(stu_num):
            student = Student(i+1, random.choice(stu_names), f"{random.randint(1, 31)}/{random.randint(1, 12)}")
            self.students.append(student)

        course_num = random.randint(3, 5)
        print(f"Enter number of courses: {course_num}")
        course_names = ["Math", "Physic", "Chemistry", "Bio", "Programming"]
        for i in range(course_num):
            course = Course(i+1, course_names[i], random.randint(1, 3))
            self.courses.append(course)

        for course in self.courses:
            marks_sheet = MarksSheet()
            for student in self.students:
                mark = random.randint(0, 20)
                marks_sheet.add_mark(student.ID, mark)
                student.set_marks(course.ID, mark)
            self.marks_sheets.append(marks_sheet)

    def courses_marks_input(self):
        course_id = int(input("Enter course ID you want to input marks: "))
        marks_sheet = self.marks_sheets[course_id - 1]
        for student in self.students:
            mark = input(f"Input mark for student {student.name}: ")
            marks_sheet.add_mark(student.ID, mark)
            student.set_marks(course_id, mark)

    def calculate_gpa(self, student_id):
        student = next((student for student in self.students if student.ID == student_id), None)
        if student:
            return student.calculate_gpa(self.courses)
        return None

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: self.calculate_gpa(student.ID), reverse=True)

    def display_students(self):
        print("Students list:")
        for student in self.students:
            print(f"ID: {student.ID}, Name: {student.name}, DoB: {student.dob}")

    def display_courses(self):
        print("Courses list:")
        for course in self.courses:
            print(f"ID: {course.ID}, Name: {course.name}, Credit: {course.credit}")

    def display_marks(self):
        course_id = int(input("Enter course ID you want to view marks for: "))
        marks_sheet = self.marks_sheets[course_id - 1]
        print(f"Marks list for course {self.courses[course_id - 1].name}:")
        for student in self.students:
            mark = marks_sheet.get_mark(student.ID)
            print(f"Student ID: {student.ID}, Name: {student.name}, Mark: {mark}")

    def run(self):
        print("Do you want to manually input or use our \"lazy input\" instead?")
        print("1. Manually")
        print("2. Lazy input")
        choice = int(input())

        if choice == 1:
            self.manual_input()
        elif choice == 2:
            self.lazy_input()

        while True:
            print("Choose your action:")
            print("1. Input marks for a course")
            print("2. Display students")
            print("3. Display courses")
            print("4. Display marks")
            print("5. Sort students by GPA")
            print("0. End the program")
            action = int(input())

            if action == 0:
                break
            elif action == 1:
                self.courses_marks_input()
            elif action == 2:
                self.display_students()
            elif action == 3:
                self.display_courses()
            elif action == 4:
                self.display_marks()
            elif action == 5:
                self.sort_students_by_gpa()
                print("Students sorted by GPA.")
                self.display_students()


main = SchoolManagementSystem()
main.run()
