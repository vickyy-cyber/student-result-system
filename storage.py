import json
from pathlib import Path
from student import Student

DATA_FILE = Path(__file__).parent / "data" / "students.json"


def load_students():
    """Load student records. Return an empty list if the file is not present."""
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        if not DATA_FILE.exists():
            return []
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return [Student.from_dict(item) for item in data]
    except json.JSONDecodeError:
        print("Warning: The data file contains invalid JSON. Starting with no records.")
        return []
    except (OSError, KeyError, TypeError) as error:
        print(f"Could not load student data: {error}")
        return []


def save_students(students):
    """Save all student records to the JSON data file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    temporary_file = DATA_FILE.with_suffix(".tmp")
    try:
        with temporary_file.open("w", encoding="utf-8") as file:
            json.dump([student.to_dict() for student in students], file, indent=4)
        temporary_file.replace(DATA_FILE)
    except OSError as error:
        print(f"Error saving student data: {error}")
        raise
