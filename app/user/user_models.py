from app import db, login
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
# from flask_login import UserMixin
# from app import login
from app import db

# @login.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id)) 
from werkzeug.security import generate_password_hash, check_password_hash

#from flask_login import UserMixin

# Stores common fields 
class User(db.Model):
    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    username: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), unique=True, nullable=False)
    email: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(120), unique=True, nullable=False)
    password_hash: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(256), nullable=False)
    first_name: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), nullable=False)
    last_name: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), nullable=False)
    phone_number: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(10), nullable=False)
    wpi_id : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(9), nullable = False)

    # Relationships 
    student_profile: sqlo.Mapped['Student'] = sqlo.relationship('Student', back_populates='user', uselist=False)
    faculty_profile: sqlo.Mapped['Faculty'] = sqlo.relationship('Faculty', back_populates='user', uselist=False)

    def __repr__(self):
        # Excluded password_hash for security
        return f"<User(id={self.id}, username='{self.username}')>"

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.password_hash, password)

# Student Model
class Student(db.Model):
    id: sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey('user.id'), primary_key=True)
    past_sa : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), nullable=False)
    major: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), nullable=False)
    cum_gpa: sqlo.Mapped[float] = sqlo.mapped_column(sqla.Float, nullable=False)
    grad_year: sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer, nullable=False)

    # One-to-one relationship
    user: sqlo.Mapped['User'] = sqlo.relationship('User', back_populates='student_profile')

    def __repr__(self):
        return f"<Student(id={self.id}, major='{self.major}')>"

# Faculty Model
class Faculty(db.Model):
    id: sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey('user.id'), primary_key=True)
    department : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), nullable=False)

    # One-to-one relationship
    user: sqlo.Mapped['User'] = sqlo.relationship('User', back_populates='faculty_profile')

    def __repr__(self):
        return f"<Faculty(id={self.id}, department='{self.department}')>"

class CourseSection(db.Model):
    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    course_code: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(10), nullable=False)
    section_number: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(5), nullable=False)
    instructor_id: sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey('faculty.id'), nullable=False)

    instructor: sqlo.Mapped['Faculty'] = sqlo.relationship('Faculty', back_populates='course_sections')
    sa_positions: sqlo.Mapped[list['SAPosition']] = sqlo.relationship('SAPosition', back_populates='course_section')

    def __repr__(self):
        return f"<CourseSection(id={self.id}, course_code='{self.course_code}', section_number='{self.section_number}')>"

class SAPosition(db.Model):
    __tablename__ = 'sa_position'

    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    course_section_id: sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey('course_section.id'), nullable=False)
    number_of_sas: sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer, nullable=False)
    qualifications: sqlo.Mapped[str] = sqlo.mapped_column(sqla.Text, nullable=False)

    course_section: sqlo.Mapped['CourseSection'] = sqlo.relationship('CourseSection', back_populates='sa_positions')

    def __repr__(self):
        return f"<SAPosition(id={self.id}, course_section_id={self.course_section_id}, number_of_sas={self.number_of_sas})>"


# Define the user_loader function in the models file
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
