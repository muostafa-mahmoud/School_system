class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.classes = []

    def enroll(self, class_name):
        self.classes.append(class_name)

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Classes: {', '.join(self.classes)}"
