from config import db 

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    school = db.Column(db.String(120), unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "fullName": self.fullname,
            "gender": self.gender,
            "school": self.school,
        }
  