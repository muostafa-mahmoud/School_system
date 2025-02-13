from school.Courses import Class
from school.Grades  import Grades
from school.Student import Student
from school.Teacher import Teacher
class System:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.classes = []
        self.grades = []

    # Adding new Students .
    def add_student(self, student_id, name):
        if not isinstance(student_id, int) or student_id <= 0:
            print("Error: Student ID must be a positive integer.")
            return None
        if any(s.student_id == student_id for s in self.students):
            print(f"Error: Student ID {student_id} already exists.")
            return None
        student = Student(student_id, name)
        self.students.append(student)
        return student

    # Adding new teachers .
    def add_teacher(self, teacher_id, name):
        if not isinstance(teacher_id, int) or teacher_id <= 0:
            print("Error: Teacher ID must be a positive integer.")
            return None
        if any(t.teacher_id == teacher_id for t in self.teachers):
            print(f"Error: Teacher ID {teacher_id} already exists.")
            return None
        teacher = Teacher(teacher_id, name)
        self.teachers.append(teacher)
        return teacher
    #Adding new classes .
    def add_class(self, class_name, subject):
        if any(c.class_name == class_name for c in self.classes):
            print(f"Error: Class {class_name} already exists.")
            return None
        new_class = Class(class_name, subject)
        self.classes.append(new_class)
        return new_class
    #Assigning students to classes .
    def enroll_student_in_class(self, student_id, class_name):
        student = next((s for s in self.students if s.student_id == student_id), None)
        class_ = next((c for c in self.classes if c.class_name == class_name), None)
        if not student:
            print(f"Error: Student with ID {student_id} not found.")
        elif not class_:
            print(f"Error: Class {class_name} not found.")
        else:
            class_.add_student(student)
    #Assigning teachers to classes .
    def assign_teacher_to_class(self, teacher_id, class_name):
        teacher = next((t for t in self.teachers if t.teacher_id == teacher_id), None)
        class_ = next((c for c in self.classes if c.class_name == class_name), None)
        if not teacher:
            print(f"Error: Teacher with ID {teacher_id} not found.")
        elif not class_:
            print(f"Error: Class {class_name} not found.")
        else:
            class_.assign_teacher(teacher)
    #Adding students grades .
    def add_grade(self, student_id, class_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if not student:
            print(f"Error: Student with ID {student_id} not found.")
            return
        class_ = next((c for c in self.classes if c.class_name == class_name), None)
        if not class_:
            print(f"Error: Class {class_name} not found.")
            return
        if student not in class_.students:
            print(f"Error: Student {student.name} is not enrolled in {class_name}.")
            return
        grades = next((g for g in self.grades if g.student.student_id == student_id and g.class_name == class_name), None)
        if not grades:
            grades = Grades(student, class_name)
            self.grades.append(grades)
        grades.add_grade(grade)

    def __str__(self):
        return (
            f"School: {self.name}\n"
            f"Students: {len(self.students)}\n"
            f"Teachers: {len(self.teachers)}\n"
            f"Classes: {len(self.classes)}\n"
            f"Grades Recorded: {len(self.grades)}\n"
        )

