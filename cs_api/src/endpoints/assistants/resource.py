from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import Assistants
from app import db


assistant_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

assistant_list_fields = {
    'count': fields.Integer,
    'assistants': fields.List(fields.Nested(assistant_fields)),
}

assistant_post_parser = reqparse.RequestParser()
assistant_post_parser.add_argument('name', type=str, required=True, location=['json'],
                              help='name parameter is required')


class AssistantResource(Resource):
    def get(self, assistant_id=None):
        if assistant_id:
            assistant = Assistants.query.filter_by(id=assistant_id).first()
            return marshal(assistant, assistant_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            assistant = Assistants.query.filter_by(**args).order_by(Assistants.id)
            if limit:
                assistant = assistant.limit(limit)

            if offset:
                assistant = assistant.offset(offset)

            assistant = assistant.all()

            return marshal({
                'count': len(assistant),
                'assistants': [marshal(u, assistant_fields) for u in assistant]
            }, assistant_list_fields)

    @marshal_with(assistant_fields)
    def post(self):
        args = assistant_post_parser.parse_args()

        assistant = Assistants(**args)
        db.session.add(assistant)
        db.session.commit()

        return assistant

    @marshal_with(assistant_fields)
    def put(self, assistant_id=None):
        assistant = Assistants.query.get(assistant_id)

        if 'name' in request.json:
            assistant.name = request.json['name']

        db.session.commit()
        return assistant

    @marshal_with(assistant_fields)
    def delete(self, assistant_id=None):
        assistant = Assistants.query.get(assistant_id)

        db.session.delete(assistant)
        db.session.commit()

        return assistant
