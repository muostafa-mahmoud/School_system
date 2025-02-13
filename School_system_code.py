class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.classes = []
    
    def enroll(self, class_name):
        self.classes.append(class_name)

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Classes: {', '.join(self.classes)}"


class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.classes_taught = []

    def assign_class(self, class_name):
        self.classes_taught.append(class_name)

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Classes Taught: {', '.join(self.classes_taught)}"


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


class Attendance:
    def __init__(self, student, class_name):
        self.student = student
        self.class_name = class_name
        self.attendance_records = []
    #Marking student's attendance
    def mark_attendance(self, date, status):
        if status.lower() in ["present", "absent"]:
            self.attendance_records.append((date, status.lower()))
        else:
            print(f"Error: Invalid attendance status '{status}'. Must be 'Present' or 'Absent'.")
    #Remodifying str function to return students records
    def __str__(self):
        records = "\n".join([f"{date}: {status}" for date, status in self.attendance_records])
        return f"Student: {self.student.name}, Class: {self.class_name}\nAttendance Records:\n{records}"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.classes = []
        self.grades = []
        self.attendance = []

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

    def mark_attendance(self, student_id, class_name, date, status):
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
        attendance = next((a for a in self.attendance if a.student.student_id == student_id and a.class_name == class_name), None)
        if not attendance:
            attendance = Attendance(student, class_name)
            self.attendance.append(attendance)
        attendance.mark_attendance(date, status)

    def __str__(self):
        return (
            f"School: {self.name}\n"
            f"Students: {len(self.students)}\n"
            f"Teachers: {len(self.teachers)}\n"
            f"Classes: {len(self.classes)}\n"
            f"Grades Recorded: {len(self.grades)}\n"
            f"Attendance Records: {len(self.attendance)}"
        )


# Menu-driven interface
def display_menu():
    print("\n===== School Management System =====")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Add Class")
    print("4. Enroll Student in Class")
    print("5. Assign Teacher to Class")
    print("6. Add Grade for Student")
    print("7. Mark Attendance")
    print("8. View All Data")
    print("9. Exit")


def main():
    school_name = input("Enter school name: ")
    school = School(school_name)

    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            school.add_student(student_id, name)

        elif choice == "2":
            teacher_id = int(input("Enter teacher ID: "))
            name = input("Enter teacher name: ")
            school.add_teacher(teacher_id, name)

        elif choice == "3":
            class_name = input("Enter class name: ")
            subject = input("Enter subject: ")
            school.add_class(class_name, subject)

        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            class_name = input("Enter class name: ")
            school.enroll_student_in_class(student_id, class_name)

        elif choice == "5":
            teacher_id = int(input("Enter teacher ID: "))
            class_name = input("Enter class name: ")
            school.assign_teacher_to_class(teacher_id, class_name)

        elif choice == "6":
            student_id = int(input("Enter student ID: "))
            class_name = input("Enter class name: ")
            grade = float(input("Enter grade: "))
            school.add_grade(student_id, class_name, grade)

        elif choice == "7":
            student_id = int(input("Enter student ID: "))
            class_name = input("Enter class name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            status = input("Enter status (Present/Absent): ")
            school.mark_attendance(student_id, class_name, date, status)

        elif choice == "8":
            print("\n===== School Data =====")
            print(school)
            print("\nStudents:")
            for student in school.students:
                print(student)
            print("\nTeachers:")
            for teacher in school.teachers:
                print(teacher)
            print("\nClasses:")
            for class_ in school.classes:
                print(class_)
            print("\nGrades:")
            for grade in school.grades:
                print(grade)
            print("\nAttendance:")
            for attendance in school.attendance:
                print(attendance)

        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()