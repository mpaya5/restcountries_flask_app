from .base_model import BaseDatabase
from database import db

db.metadata.schema = 'orig'

class StudentsDatabase(BaseDatabase):
    __tablename__ = "students"

    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)


class LanguagesDatabase(BaseDatabase):
    __tablename__ = "languages"
    
    name = db.Column(db.String(255), nullable=False)


class StudentLanguagesDatabase(BaseDatabase):
    __tablename__ = "student_languages"

    student_id = db.Column(db.Integer, db.ForeignKey('orig.students.id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('orig.languages.id'), nullable=False)