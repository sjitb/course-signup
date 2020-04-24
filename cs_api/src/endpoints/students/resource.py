from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import Students
from app import db

student_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

student_list_fields = {
    'count': fields.Integer,
    'students': fields.List(fields.Nested(student_fields)),
}

student_post_parser = reqparse.RequestParser()
student_post_parser.add_argument('name', type=str, required=True, location=['json'],
                              help='name parameter is required')


class StudentsResource(Resource):
    def get(self, student_id=None):
        if student_id:
            student = Students.query.filter_by(id=student_id).first()
            return marshal(student, student_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            student = Students.query.filter_by(**args).order_by(Students.id)
            if limit:
                student = student.limit(limit)

            if offset:
                student = student.offset(offset)

            student = student.all()

            return marshal({
                'count': len(student),
                'students': [marshal(u, student_fields) for u in student]
            }, student_list_fields)

    @marshal_with(student_fields)
    def post(self):
        args = student_post_parser.parse_args()

        student = Students(**args)
        db.session.add(student)
        db.session.commit()

        return student

    @marshal_with(student_fields)
    def put(self, student_id=None):
        student = Students.query.get(student_id)

        if 'name' in request.json:
            student.name = request.json['name']

        db.session.commit()
        return student

    @marshal_with(student_fields)
    def delete(self, student_id=None):
        student = Students.query.get(student_id)

        db.session.delete(student)
        db.session.commit()

        return student
