from app import db


class Professors(db.Model):
    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


    def __repr__(self):
        return 'Id: {}, name: {}'.format(self.id, self.name)
