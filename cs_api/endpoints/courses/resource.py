from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import Courses
from app import db

course_fields = {
    'Id': fields.String,
    'Name': fields.String,
    'Department_Name': fields.String,
    'Semester' : fields.String,
    'Year' : fields.Integer,
    'Is_Active': fields.Integer,
    'Department_Id': fields.Integer,
    'Department': fields.List(fields.Nested({'Id': fields.Integer,
                                        'Name': fields.String})),
}

            
course_list_fields = {
    'count': fields.Integer,
    'courses': fields.List(fields.Nested(course_fields)),
}

course_post_parser = reqparse.RequestParser()
course_post_parser.add_argument('Id', type=str, required=True, location=['json'],
                              help='Id parameter is required')
course_post_parser.add_argument('Name', type=str, required=True, location=['json'],
                              help='Name parameter is required')
course_post_parser.add_argument('Department_Name', type=str, required=True, location=['json'],
                              help='Department Name parameter is required')
course_post_parser.add_argument('Semester', type=str, required=True, location=['json'],
                              help='Semester parameter is required')
course_post_parser.add_argument('Year', type=int, required=True, location=['json'],
                              help='Year parameter is required')
course_post_parser.add_argument('Is_Active', type=int, required=False, location=['json'])
course_post_parser.add_argument('Department_Id', type=int, required=False, location=['json'])


class CoursesResource(Resource):
    def get(self, course_id=None):
        if course_id:
            course = Courses.query.filter_by(id=course_id).first()
            return marshal(course, course_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            course = Courses.query.filter_by(**args).order_by(Courses.id)
            if limit:
                course = course.limit(limit)

            if offset:
                course = course.offset(offset)

            course = course.all()

            return marshal({
                'count': len(course),
                'courses': [marshal(c, course_fields) for c in course]
            }, course_list_fields)

    @marshal_with(course_fields)
    def post(self):
        args = course_post_parser.parse_args()

        course = Courses(**args)
        db.session.add(course)
        db.session.commit()

        return course

    @marshal_with(course_fields)
    def put(self, course_id=None):
        course = Courses.query.get(course_id)

        if 'Id' in request.json:
            course.Id = request.json['Id']

        db.session.commit()
        return course

    @marshal_with(user_fields)
    def delete(self, course_id=None):
        course = Courses.query.get(course_id)

        db.session.delete(course)
        db.session.commit()

        return course
