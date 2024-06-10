from flask import request, jsonify
from config import app, db
from models import Student

@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    json_students = list(map(lambda x: x.to_json(), students))
    return jsonify({"students": json_students})
@app.route("/create_student", methods=["POST"])
def create_students():
    fullname = request.json.get("fullName")
    gender = request.json.get("gender")
    school = request.json.get("school")

    if not fullname or not gender or not school:
        return (jsonify ({"message": "You must provide all essential information"}),400,)
    new_student = Student(fullname=fullname, gender=gender, school=school)
    try: 
        db.session.add(new_student)
        db.session.commit()
    except Exception as e:
        return jsonify ({"message": str(e)}), 400
    return jsonify({"message": "Student created!"}), 201
@app.route("/update_student/<int:user_id>", methods=["PATCH"])
def update_students(user_id):
    student = Student.query.get(user_id)

    if not student:
        return jsonify({"message": "Student Not Found!"}), 404
    
    data = request.json
    student.fullname = data.get("fullName", student.fullname)
    student.gender = data.get("gender", student.gender)
    student.school = data.get("school", student.school)

    db.session.commit()

    return jsonify({"message": "Student updated!"}), 200
@app.route("/delete_student/<int:user_id>", methods=["DELETE"])
def delete_student(user_id):
    student = Student.query.get(user_id)

    if not student:
        return jsonify({"message": "user not found"}), 404
    db.session.delete(student)
    db.session.commit()
    return  jsonify({"message": "Student deleted!"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all() #
    app.run(host="0.0.0.0",debug=True)