from datetime import datetime

# The system uses five subjects. You can change these names if your school
# uses a different set of subjects.
SUBJECTS = ["English", "Mathematics", "Biology", "Chemistry", "Physics"]


def record_scores(student, scores):
    """Save five subject scores and record the date they were entered."""
    if len(scores) != len(SUBJECTS):
        raise ValueError("Exactly five subject scores are required.")

    for subject in SUBJECTS:
        score = float(scores[subject])
        if not 0 <= score <= 100:
            raise ValueError(f"{subject} score must be between 0 and 100.")

    student.scores = {subject: float(scores[subject]) for subject in SUBJECTS}
    student.result_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate_total(student):
    if not student.scores:
        return 0
    return sum(float(value) for value in student.scores.values())


def calculate_average(student):
    if not student.scores:
        return 0
    return calculate_total(student) / len(student.scores)


def assign_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    return "F"


def result_summary(student):
    average = calculate_average(student)
    return {
        "total": calculate_total(student),
        "average": average,
        "grade": assign_grade(average)
    }
