from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import Departments
from app import db

department_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'todos': fields.List(fields.Nested({'id': fields.Integer,
                                        'name': fields.String,
                                        'description': fields.String})),
}

department_list_fields = {
    'count': fields.Integer,
    'users': fields.List(fields.Nested(department_fields)),
}

department_post_parser = reqparse.RequestParser()
department_post_parser.add_argument('name', type=str, required=True, location=['json'],
                              help='name parameter is required')


class UsersResource(Resource):
    def get(self, department_id=None):
        if department_id:
            department = Departments.query.filter_by(id=department_id).first()
            return marshal(department, department_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            department = Departments.query.filter_by(**args).order_by(Departments.id)
            if limit:
                department = department.limit(limit)

            if offset:
                department = department.offset(offset)

            department = department.all()

            return marshal({
                'count': len(department),
                'users': [marshal(d, department_fields) for d in department]
            }, department_list_fields)

    @marshal_with(user_fields)
    def post(self):
        args = department_post_parser.parse_args()

        department = Departments(**args)
        db.session.add(department)
        db.session.commit()

        return department

    @marshal_with(department_fields)
    def put(self, department_id=None):
        department = Departments.query.get(department_id)

        if 'name' in request.json:
            department.name = request.json['name']

        db.session.commit()
        return department

    @marshal_with(department_fields)
    def delete(self, department_id=None):
        department = Departments.query.get(department_id)

        db.session.delete(department)
        db.session.commit()

        return department
