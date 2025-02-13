class Class:
    def __init__(self, class_name, subject):
        self.class_name = class_name
        self.subject = subject
        self.teacher = None
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll(self.class_name)
        else:
            print(f"Error: Student {student.name} is already enrolled in {self.class_name}.")

    def assign_teacher(self, teacher):
        if self.teacher is None:
            self.teacher = teacher
            teacher.assign_class(self.class_name)
        else:
            print(f"Error: Class {self.class_name} already has a teacher assigned.")

    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else "None"
        return f"Class: {self.class_name}, Subject: {self.subject}, Teacher: {teacher_name}, Students: {len(self.students)}"

