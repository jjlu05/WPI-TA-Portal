import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
# from flask_login import UserMixin
# from app import login
from app import db


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


# @login.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id)) 