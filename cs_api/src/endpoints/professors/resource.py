from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import Professors
from app import db

professor_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

professor_list_fields = {
    'count': fields.Integer,
    'professors': fields.List(fields.Nested(professor_fields)),
}

professor_post_parser = reqparse.RequestParser()
professor_post_parser.add_argument('name', type=str, required=True, location=['json'],
                              help='name parameter is required')


class ProfessorsResource(Resource):
    def get(self, professor_id=None):
        if professor_id:
            professor = Professors.query.filter_by(id=professor_id).first()
            return marshal(professor, professor_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            professor = Professors.query.filter_by(**args).order_by(Professors.id)
            if limit:
                professor = professor.limit(limit)

            if offset:
                professor = professor.offset(offset)

            professor = professor.all()

            return marshal({
                'count': len(professor),
                'users': [marshal(p, professor_fields) for p in professor]
            }, professor_list_fields)

    @marshal_with(professor_fields)
    def post(self):
        args = professor_post_parser.parse_args()

        professor = Professors(**args)
        db.session.add(professor)
        db.session.commit()

        return professor

    @marshal_with(professor_fields)
    def put(self, professor_id=None):
        professor = Professors.query.get(professor_id)

        if 'name' in request.json:
            professor.name = request.json['name']

        db.session.commit()
        return professor

