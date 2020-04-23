from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
import settings

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)


app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['BUNDLE_ERRORS'] = settings.BUNDLE_ERRORS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

print(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)
api = Api(app)
api.prefix = '/api'



from endpoints.assistants.resource import AssistantResource
from endpoints.courses.resource import CourseResource
from endpoints.courses.resource import CourseResource
from endpoints.courses.resource import CourseResource
from endpoints.courses.resource import CourseResource


api.add_resource(AssistantResource, '/assistants', '/assistants/<int:assistant_id>')
api.add_resource(CourseResource, '/courses', '/courses/<int:course_id>')

if __name__ == '__main__':
    app.run()