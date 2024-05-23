from flask import Blueprint, request, jsonify
from db.models import db, Student

api = Blueprint('api', __name__)

@api.route('/students', methods=['GET'])
def list_students():
    students = Student.query.all()
    return jsonify([student.as_dict() for student in students])

@api.route('/student/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.as_dict())

@api.route('/student', methods=['POST'])
def create_student():
    data = request.json
    new_student = Student(
        full_name=data['full_name'],
        gender=data['gender'],
        school=data['school']
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.as_dict()), 201

@api.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.json
    student.full_name = data.get('full_name', student.full_name)
    student.gender = data.get('gender', student.gender)
    student.school = data.get('school', student.school)
    db.session.commit()
    return jsonify(student.as_dict())

@api.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return '', 204
