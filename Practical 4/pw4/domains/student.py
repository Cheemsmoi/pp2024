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
