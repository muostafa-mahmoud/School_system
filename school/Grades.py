class Grades:
    def __init__(self, student, class_name):
        self.student = student
        self.class_name = class_name
        self.grades = []

    def add_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"Error: Grade {grade} is invalid. Must be a number between 0 and 100.")

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student: {self.student.name}, Class: {self.class_name}, Grades: {self.grades}, Average: {self.average_grade()}"