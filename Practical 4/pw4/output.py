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