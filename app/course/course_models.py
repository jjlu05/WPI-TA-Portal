from app import db, login
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

# Course Section Model
class CourseSection(db.Model):
    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    course_code: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(10), nullable=False)
    section_number: sqlo.Mapped[int] = sqlo.mapped_column(nullable=False)
    instructor_id: sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey('faculty.id'))
    term: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(5), nullable=False)

    # Relationships
    instructor: sqlo.Mapped['Faculty'] = sqlo.relationship('Faculty', back_populates='course_sections')
    sa_positions: sqlo.Mapped[list['SAPosition']] = sqlo.relationship('SAPosition', back_populates='course_section')

    def __repr__(self):
        return f"<CourseSection(id={self.id}, course_code='{self.course_code}', section_number='{self.section_number}')>"


class Course(db.Model):
    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    major: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(10))
    coursenum: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(4))



