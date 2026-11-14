from datetime import datetime


class Student:
    """Represents one student and the student's academic records."""

    def __init__(self, student_id, full_name, class_form, gender, date_of_birth,
                 scores=None, result_date=None):
        self.student_id = student_id.strip()
        self.full_name = full_name.strip()
        self.class_form = class_form.strip()
        self.gender = gender.strip()
        self.date_of_birth = date_of_birth.strip()
        self.scores = scores or {}
        self.result_date = result_date

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "class_form": self.class_form,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth,
            "scores": self.scores,
            "result_date": self.result_date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["full_name"],
            data["class_form"],
            data["gender"],
            data["date_of_birth"],
            data.get("scores", {}),
            data.get("result_date")
        )
