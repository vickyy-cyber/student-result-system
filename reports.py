from results import calculate_total, calculate_average, assign_grade


def display_student_report(student):
    print("\n" + "=" * 48)
    print("                 STUDENT REPORT CARD")
    print("=" * 48)
    print(f"Student ID      : {student.student_id}")
    print(f"Full Name       : {student.full_name}")
    print(f"Class/Form      : {student.class_form}")
    print(f"Gender          : {student.gender}")
    print(f"Date of Birth   : {student.date_of_birth}")
    print("-" * 48)

    if not student.scores:
        print("No scores have been recorded for this student.")
    else:
        for subject, score in student.scores.items():
            print(f"{subject:<20}: {score:>6.1f}")
        average = calculate_average(student)
        print("-" * 48)
        print(f"{'Total':<20}: {calculate_total(student):>6.1f}")
        print(f"{'Average':<20}: {average:>6.2f}")
        print(f"{'Grade':<20}: {assign_grade(average)}")
        print(f"Result entered     : {student.result_date or 'Not recorded'}")
    print("=" * 48)


def list_student_results(students):
    if not students:
        print("No students are registered.")
        return
    print("\nSTUDENT RESULTS")
    print("-" * 76)
    print(f"{'ID':<12}{'NAME':<24}{'TOTAL':>10}{'AVERAGE':>12}{'GRADE':>10}")
    print("-" * 76)
    for student in students:
        if student.scores:
            total = calculate_total(student)
            average = calculate_average(student)
            grade = assign_grade(average)
            print(f"{student.student_id:<12}{student.full_name[:22]:<24}"
                  f"{total:>10.1f}{average:>12.2f}{grade:>10}")
        else:
            print(f"{student.student_id:<12}{student.full_name[:22]:<24}"
                  f"{'No scores':>10}{'-':>12}{'-':>10}")


def show_class_statistics(students):
    completed = [student for student in students if student.scores]
    if not completed:
        print("There are no recorded results to analyse.")
        return

    averages = [calculate_average(student) for student in completed]
    highest = max(completed, key=calculate_average)
    lowest = min(completed, key=calculate_average)
    class_average = sum(averages) / len(averages)

    print("\nCLASS STATISTICS")
    print("-" * 40)
    print(f"Students with results : {len(completed)}")
    print(f"Highest average       : {calculate_average(highest):.2f} ({highest.full_name})")
    print(f"Lowest average        : {calculate_average(lowest):.2f} ({lowest.full_name})")
    print(f"Class average         : {class_average:.2f}")


def save_text_report(students):
    """Create a text report in the project folder."""
    from pathlib import Path
    report_file = Path(__file__).parent / "student_results_report.txt"
    with report_file.open("w", encoding="utf-8") as file:
        file.write("STUDENT RESULT MANAGEMENT SYSTEM REPORT\n")
        file.write("=" * 55 + "\n")
        for student in students:
            file.write(f"\nID: {student.student_id}\n")
            file.write(f"Name: {student.full_name}\n")
            file.write(f"Class/Form: {student.class_form}\n")
            if student.scores:
                file.write(f"Scores: {student.scores}\n")
                file.write(f"Total: {calculate_total(student):.1f}\n")
                file.write(f"Average: {calculate_average(student):.2f}\n")
                file.write(f"Grade: {assign_grade(calculate_average(student))}\n")
            else:
                file.write("Scores: Not yet recorded\n")
            file.write("-" * 55 + "\n")
    print(f"Text report saved successfully as: {report_file.name}")


def sort_students(students, choice):
    if choice == "1":
        return sorted(students, key=calculate_average, reverse=True)
    return sorted(students, key=lambda student: student.full_name.lower())
