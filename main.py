from datetime import datetime
from student import Student
from results import SUBJECTS, record_scores
from storage import load_students, save_students
from reports import (
    display_student_report,
    list_student_results,
    show_class_statistics,
    save_text_report,
    sort_students
)


def get_student_by_id(students, student_id):
    for student in students:
        if student.student_id.lower() == student_id.strip().lower():
            return student
    return None


def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Try again.")


def read_date(prompt):
    while True:
        value = input(prompt).strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Enter the date in YYYY-MM-DD format, for example 2005-04-18.")


def add_student(students):
    print("\nADD NEW STUDENT")
    student_id = read_non_empty("Student ID: ")
    if get_student_by_id(students, student_id):
        print("A student with that ID already exists.")
        return

    full_name = read_non_empty("Full name: ")
    class_form = read_non_empty("Class/Form: ")
    gender = read_non_empty("Gender: ")
    date_of_birth = read_date("Date of birth (YYYY-MM-DD): ")

    students.append(Student(student_id, full_name, class_form, gender, date_of_birth))
    save_students(students)
    print("Student registered successfully.")


def view_students(students):
    if not students:
        print("No students are registered.")
        return
    print("\nREGISTERED STUDENTS")
    print("-" * 65)
    for student in students:
        print(f"ID: {student.student_id} | Name: {student.full_name} | "
              f"Class: {student.class_form} | Gender: {student.gender}")


def search_student(students):
    term = input("Enter student ID or part of the student's name: ").strip().lower()
    matches = [
        student for student in students
        if term in student.student_id.lower() or term in student.full_name.lower()
    ]
    if not matches:
        print("No matching student was found.")
        return
    for student in matches:
        display_student_report(student)


def update_student(students):
    student_id = input("Enter the ID of the student to update: ").strip()
    student = get_student_by_id(students, student_id)
    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")
    name = input(f"Full name [{student.full_name}]: ").strip()
    class_form = input(f"Class/Form [{student.class_form}]: ").strip()
    gender = input(f"Gender [{student.gender}]: ").strip()
    dob = input(f"Date of birth [{student.date_of_birth}] (YYYY-MM-DD): ").strip()

    if name:
        student.full_name = name
    if class_form:
        student.class_form = class_form
    if gender:
        student.gender = gender
    if dob:
        try:
            datetime.strptime(dob, "%Y-%m-%d")
            student.date_of_birth = dob
        except ValueError:
            print("Invalid date. The previous date of birth was kept.")

    save_students(students)
    print("Student information updated.")


def delete_student(students):
    student_id = input("Enter the ID of the student to delete: ").strip()
    student = get_student_by_id(students, student_id)
    if not student:
        print("Student not found.")
        return
    confirm = input(f"Delete {student.full_name}? Type YES to confirm: ").strip()
    if confirm == "YES":
        students.remove(student)
        save_students(students)
        print("Student record deleted.")
    else:
        print("Deletion cancelled.")


def enter_or_update_scores(students):
    student_id = input("Enter student ID: ").strip()
    student = get_student_by_id(students, student_id)
    if not student:
        print("Student not found.")
        return

    print(f"Enter scores for {student.full_name}. Scores must be from 0 to 100.")
    scores = {}
    for subject in SUBJECTS:
        while True:
            try:
                score = float(input(f"{subject}: "))
                if not 0 <= score <= 100:
                    print("Score must be between 0 and 100.")
                    continue
                scores[subject] = score
                break
            except ValueError:
                print("Please enter a valid number.")

    record_scores(student, scores)
    save_students(students)
    print("Scores saved successfully.")


def individual_report(students):
    student_id = input("Enter student ID: ").strip()
    student = get_student_by_id(students, student_id)
    if student:
        display_student_report(student)
    else:
        print("Student not found.")


def main():
    students = load_students()
    print("Welcome to the Student Result Management System")

    while True:
        print("\n" + "=" * 48)
        print("       STUDENT RESULT MANAGEMENT SYSTEM")
        print("=" * 48)
        print("1. Add a new student")
        print("2. View all students")
        print("3. Search for a student")
        print("4. Update student information")
        print("5. Delete a student")
        print("6. Record / Update five subject scores")
        print("7. Display an individual report card")
        print("8. List all student results")
        print("9. Sort students")
        print("10. Show class statistics")
        print("11. Save a text report")
        print("0. Save and exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                add_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                enter_or_update_scores(students)
            elif choice == "7":
                individual_report(students)
            elif choice == "8":
                list_student_results(students)
            elif choice == "9":
                print("1. Average score (highest to lowest)")
                print("2. Student name (A to Z)")
                sort_choice = input("Choose sorting method: ").strip()
                if sort_choice in ("1", "2"):
                    sorted_list = sort_students(students, sort_choice)
                    view_students(sorted_list)
                else:
                    print("Invalid sorting choice.")
            elif choice == "10":
                show_class_statistics(students)
            elif choice == "11":
                save_text_report(students)
            elif choice == "0":
                save_students(students)
                print("All records saved. Goodbye!")
                break
            else:
                print("Invalid option. Choose a number from the menu.")
        except (ValueError, OSError) as error:
            print(f"An error occurred: {error}")
        else:
            # The selected operation completed without an uncaught error.
            pass
        finally:
            # This block runs after each menu operation.
            pass


if __name__ == "__main__":
    main()
