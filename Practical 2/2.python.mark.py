import random

class Student:
    def __init__(self, ID, name, dob):
        self.ID = ID
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

class MarksSheet:
    def __init__(self):
        self.marks = []

    def add_mark(self, student, mark):
        self.marks.append({'Student_ID': student.ID, 'Student_name': student.name, 'Mark': mark})

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
            course = Course(input("Enter course ID: "), input("Enter course name: "))
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
            course = Course(i+1, course_names[i])
            self.courses.append(course)

        for course in self.courses:
            marks_sheet = MarksSheet()
            for student in self.students:
                mark = random.randint(0, 20)
                marks_sheet.add_mark(student, mark)
            self.marks_sheets.append(marks_sheet)

    def courses_marks_input(self):
        course_id = int(input("Enter course ID you want to input marks: "))
        marks_sheet = self.marks_sheets[course_id - 1]
        for i, mark_entry in enumerate(marks_sheet.marks):
            mark = input(f"Input student {i+1} mark: ")
            mark_entry['Mark'] = mark

    def display(self):
        print("Choose what you want to display:")
        print("1. Students list")
        print("2. Courses list")
        print("3. Marks list")

        choice = int(input())

        if choice == 1:
            print("Students list:")
            for student in self.students:
                print(f"ID: {student.ID}, Name: {student.name}, DoB: {student.dob}")
        elif choice == 2:
            print("Courses list:")
            for course in self.courses:
                print(f"ID: {course.ID}, Name: {course.name}")
        elif choice == 3:
            course_id = int(input("Enter course ID you want to view marks for: "))
            marks_sheet = self.marks_sheets[course_id - 1]
            print(f"Marks list for course {self.courses[course_id - 1].name}:")
            for mark_entry in marks_sheet.marks:
                print(f"Student ID: {mark_entry['Student_ID']}, Name: {mark_entry['Student_name']}, Mark: {mark_entry['Mark']}")

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
            print("2. Display")
            print("0. End the program")
            action = int(input())

            if action == 0:
                break
            elif action == 1:
                self.courses_marks_input()
            elif action == 2:
                self.display()

#main
main = SchoolManagementSystem()
main.run()
