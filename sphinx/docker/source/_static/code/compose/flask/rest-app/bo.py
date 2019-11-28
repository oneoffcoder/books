import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=50))
    last_name = sqlalchemy.Column(sqlalchemy.String(length=50))
    gender = sqlalchemy.Column(sqlalchemy.String(length=1))

    @staticmethod
    def instance(first_name, last_name, gender):
        s = Student(first_name=first_name, last_name=last_name, gender=gender)
        return s

    def dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender
        }

    def __repr__(self):
        return f'<Student(first_name={self.first_name}, last_name={self.last_name}, gender={self.gender})>'