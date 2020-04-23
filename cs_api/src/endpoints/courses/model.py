from app import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class Courses(db.Model):
    __tablename__ = "course"

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    department = db.Column(db.String, nullable=False)
    semester = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, nullable=True)
    

    #departmentR = db.relationship('department', backref='department.id', primaryjoin='course.department_id==department.id', lazy='joined')



    def __repr__(self):
        return 'Id: {}, Name: {}, Department_Name: {}, Semester: {}, Year: {}, Is_Active: {}, Department_Id'.format(
            self.id, self.name, self.department_name, self.semester, self.year, self.is_active, self.department_id
            )
