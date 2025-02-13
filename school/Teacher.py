class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.classes_taught = []

    def assign_class(self, class_name):
        self.classes_taught.append(class_name)

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Classes Taught: {', '.join(self.classes_taught)}"

