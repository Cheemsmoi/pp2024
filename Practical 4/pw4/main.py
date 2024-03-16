from pw4.input import manual_input, lazy_input
from pw4.output import display_students, display_courses, display_marks
from pw4.domains.school_management_system import SchoolManagementSystem

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