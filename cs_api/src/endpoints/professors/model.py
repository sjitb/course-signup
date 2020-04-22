from app import db


class Professors(db.Model):
    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email_id = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=True)
    is_active = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return 'Id: {}, Name: {}'.format(self.id, self.name)
