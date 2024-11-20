from app import db, login
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 

# Stores common fields 
class User(db.Model):
    __abstract__ = True

    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    username: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), unique=True, nullable=False)
    email: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(120), unique=True, nullable=False)
    password_hash: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(256), nullable=False)
    first_name: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), nullable=False)
    last_name: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), nullable=False)
    phone_number: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(10), nullable=False)
    wpi_id : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(9), nullable = False)

    def __repr__(self):
        # Excluded password_hash for security
        return f"<User(id={self.id}, username='{self.username}')>"

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.password_hash, password)

# Student Model
class Student(User):
    major: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), default="none", nullable=False)
    cum_gpa: sqlo.Mapped[float] = sqlo.mapped_column(sqla.Float, default=0, nullable=False)
    grad_year: sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer, default=0, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, major='{self.major}')>"

# Faculty Model
class Faculty(User):
    department : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), default="none", nullable=False)

    def __repr__(self):
        return f"<Faculty(id={self.id}, department='{self.department}')>"

class CourseSection(db.Model):
    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    # course_code: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(10), nullable=False)
    # section_number: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(5), nullable=False)
    # instructor_id: sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey('faculty.id'), nullable=False)

    # instructor: sqlo.Mapped['Faculty'] = sqlo.relationship('Faculty', back_populates='course_sections')
    # sa_positions: sqlo.Mapped[list['SAPosition']] = sqlo.relationship('SAPosition', back_populates='course_section')

    # def __repr__(self):
    #     return f"<CourseSection(id={self.id}, course_code='{self.course_code}', section_number='{self.section_number}')>"

class SAPosition(db.Model):
    __tablename__ = 'sa_position'

    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    # course_section_id: sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey('course_section.id'), nullable=False)
    # number_of_sas: sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer, nullable=False)
    # qualifications: sqlo.Mapped[str] = sqlo.mapped_column(sqla.Text, nullable=False)

    # course_section: sqlo.Mapped['CourseSection'] = sqlo.relationship('CourseSection', back_populates='sa_positions')

    # def __repr__(self):
    #     return f"<SAPosition(id={self.id}, course_section_id={self.course_section_id}, number_of_sas={self.number_of_sas})>"


class Course(db.Model):
    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    term: sqlo.Mapped[str] = sqlo.mapped_column(primary_key=True)
    section: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    coursenum: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(4), primary_key=True)


