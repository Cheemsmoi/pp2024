class MarksSheet:
    def __init__(self):
        self.marks = {}

    def add_mark(self, student_id, mark):
        self.marks[student_id] = mark

    def get_mark(self, student_id):
        return self.marks.get(student_id, None)
