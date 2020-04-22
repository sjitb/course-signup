from app import db


class User(db.Model):
    __tablename__ = 'assistant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email_id = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=True)
    is_active = db.Column(db.Integer, nullable=False)

    courseR = db.relationship(
        'course_assistant', 
        backref='course_assistant.assistant_id', 
        primaryjoin='course_assistant.assistant_id==assistant.id', 
        lazy='joined')
    
    def __repr__(self):
        return 'Id: {}, Name: {}, Email_Id: {}, Phone: {}, Is_Active: {}'.format(
            self.id, 
            self.name,
            self.email_id,
            self.phone,
            self.is_active
            )
