from flask import Flask, render_template, request, redirect, url_for, flash
from pathlib import Path
import json
from statistics import mean

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "students.json"
SUBJECTS = ["English", "Mathematics", "Biology", "Chemistry", "Physics"]

def load_students():
    DATA_DIR.mkdir(exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []

def save_students(students):
    DATA_DIR.mkdir(exist_ok=True)
    DATA_FILE.write_text(json.dumps(students, indent=4), encoding="utf-8")

def grade(score):
    if score >= 70: return "A"
    if score >= 60: return "B"
    if score >= 50: return "C"
    if score >= 45: return "D"
    return "F"

def calculate(scores):
    total = sum(scores.values())
    average = total / len(SUBJECTS)
    return total, average, grade(average)

@app.route("/")
def index():
    students = load_students()
    for student in students:
        total, average, overall_grade = calculate(student["scores"])
        student["total"], student["average"], student["grade"] = total, round(average, 2), overall_grade
    sort_by = request.args.get("sort", "name")
    if sort_by == "average":
        students.sort(key=lambda s: s["average"], reverse=True)
    else:
        students.sort(key=lambda s: s["name"].lower())
    class_average = round(mean([s["average"] for s in students]), 2) if students else 0
    return render_template("index.html", students=students, subjects=SUBJECTS,
                           class_average=class_average, sort_by=sort_by)

@app.route("/add", methods=["POST"])
def add_student():
    students = load_students()
    student_id = request.form.get("student_id", "").strip()
    name = request.form.get("name", "").strip()
    student_class = request.form.get("student_class", "").strip()
    gender = request.form.get("gender", "").strip()
    dob = request.form.get("dob", "").strip()
    if not all([student_id, name, student_class, gender, dob]):
        flash("Please complete all student details.")
        return redirect(url_for("index"))
    if any(s["student_id"].lower() == student_id.lower() for s in students):
        flash("That student ID already exists.")
        return redirect(url_for("index"))
    scores = {}
    try:
        for subject in SUBJECTS:
            score = float(request.form.get(subject, ""))
            if not 0 <= score <= 100:
                raise ValueError
            scores[subject] = score
    except (ValueError, TypeError):
        flash("Enter a valid score from 0 to 100 for every subject.")
        return redirect(url_for("index"))
    students.append({"student_id": student_id, "name": name, "class": student_class,
                     "gender": gender, "dob": dob, "scores": scores})
    save_students(students)
    flash("Student and results saved successfully.")
    return redirect(url_for("index"))

@app.route("/student/<student_id>")
def student_report(student_id):
    students = load_students()
    student = next((s for s in students if s["student_id"] == student_id), None)
    if not student:
        flash("Student not found.")
        return redirect(url_for("index"))
    total, average, overall_grade = calculate(student["scores"])
    subject_rows = [{"name": subject, "score": student["scores"][subject],
                     "grade": grade(student["scores"][subject])} for subject in SUBJECTS]
    return render_template("report.html", student=student, rows=subject_rows,
                           total=total, average=round(average, 2), overall_grade=overall_grade)

@app.route("/delete/<student_id>", methods=["POST"])
def delete_student(student_id):
    students = load_students()
    remaining = [s for s in students if s["student_id"] != student_id]
    save_students(remaining)
    flash("Student record deleted.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
