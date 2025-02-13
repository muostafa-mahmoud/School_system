from school.display_menu import display_menu
from school.main import System
def main():
    school_name = input("Enter school name: ")
    school = System(school_name)

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


        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
