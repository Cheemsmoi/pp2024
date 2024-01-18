import random

def Init():
    global Student_list
    global Courses_list
    global Marks_sheet_list
    Student_list = []
    Courses_list = []
    
    Stu_num = int(input("Enter number of student in class: "))
    for i in range(Stu_num):
        student = {}
        student['ID'] = input("Enter student ID: ")
        student['Name'] = input("Enter student name: ")
        student['DoB'] = input("Enter student DoB: ")
        Student_list.append(student)
    print("\n")
    
    Course_num = int(input("Enter number of courses: "))
    for i in range(Course_num):
        course = {}
        course['ID'] = input("Enter course ID: ")
        course['Course name'] = input("Enter course name: ")
        Courses_list.append(course)
    Marks_sheet_list = ["" for i in range(Course_num)]
    print("\n")
    
def Lazy_input():
    global Student_list
    global Courses_list
    global Marks_sheet_list
    Student_list = []
    Courses_list = []
    
    Stu_num = random.randint(5, 10)
    print(f"Enter number of student in class: {Stu_num}")
    Stu_name = ["Alex", "Ben", "Charlie", "Dan", "Frank"]
    for i in range(Stu_num):
        student = {}
        student['ID'] = i+1
        print(f"Enter course ID: {student['ID']}")
        student['Name'] = random.choice(Stu_name)
        print(f"Enter student name: {student['Name']} ")
        student['DoB'] = f"{random.randint(1, 31)}/{random.randint(1, 12)}"
        print(f"Enter student DoB: {student['DoB']}")
        Student_list.append(student)
    print("\n")
    
    Course_num = random.randint(3, 5)
    print(f"Enter number of courses: {Course_num}")
    Course_name = ["Math", "Physic", "Chemistry", "Bio", "Programming"]
    for i in range(Course_num):
        course = {}
        course['ID'] = i+1
        print(f"Enter course ID: {course['ID']}")
        course['Course name'] = Course_name[i]
        print(f"Enter course name: {Course_name[i]}")
        Courses_list.append(course)
    Marks_sheet_list = ["" for i in range(Course_num)]
    print("\n")
    
    for j in range(Course_num):
        ID = j+1
        print(f"Enter course ID you want to input marks: {ID}")
        Marks_sheet = []
        for i in range(len(Student_list)):
            Marks_dict = {}
            Marks_dict['Student_ID'] =  Student_list[i]['ID']
            Marks_dict['Student_name'] =  Student_list[i]['Name']
            Marks_dict['Mark'] =  random.randint(0, 20)
            print(f"input student {i+1} mark: {Marks_dict['Mark']}")
            Marks_sheet.append(Marks_dict)
        Marks_sheet_list[ID-1] = Marks_sheet
        print("\n")

def courses_marks_input():
    ID = int(input("Enter course ID you want to input marks:"))
    Marks_sheet = []
    for i in range(len(Student_list)):
        Marks_dict = {}
        Marks_dict['Student_ID'] =  Student_list[i]['ID']
        Marks_dict['Student_name'] =  Student_list[i]['Name']
        Marks_dict['Mark'] =  input(f"input student {i+1} mark: ")
        Marks_sheet.append(Marks_dict)
    Marks_sheet_list[ID-1] = Marks_sheet
    print("\n")

def display(List):
    for item in List:
        print(item)
    print("\n")
        
def navigation(location):
    if location == "Menu":    
        print("Choose your action:")
        print("0/ End the programs")
        print("1/ Input marks for a course")
        print("2/ Display")
        print("\n")
        k = int(input())
        return k
        
    if location == "Display":
        print("What do you want to display:")
        print("0/ Go back")
        print("1/ Students list")
        print("2/ Courses list")
        print("3/ Marks list")
        print("\n")
        k = int(input())
        return k
    
    if location == "Marks_view":
        print("Input course ID you want to view marks: ")
        print("\n")
        k = int(input())
        return k
    
# Main:  
print("Do you want to manually input or use our \"lazy input\" instead?")
print("1/ Manually")
print("2/ Lazy input")
k = int(input())
if k == 1:
    Init()
elif k == 2:
    Lazy_input()
k0 = -1
while k0 != 0:
    k0 = navigation("Menu")
    if k0 == 1:
        courses_marks_input()
    elif k0 == 2:
        k1 = navigation("Display")
        if k1 == 0:
            continue
        elif k1 == 1:
            print("Student list:")
            display(Student_list)
        elif k1 == 2:
            print("Courses list:")
            display(Courses_list)
        elif k1 == 3:
            ID = navigation("Marks_view")
            print(f"Marks list of {Courses_list[ID-1]['Course name']} course:")
            display(Marks_sheet_list[ID-1])
print("Programs end!")