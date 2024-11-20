from app import db, login
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from app.user.user_models import Student

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
<<<<<<< HEAD
    major: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(10))
    coursenum: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(4))

    #relationship
    experiences : sqlo.WriteOnlyMapped['CourseExperience'] = sqlo.relationship(back_populates= 'course')

# Course Experience Model
class CourseExperience(db.Model):
    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    courseid : sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey(Course.id), index = True)
    userid : sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey(Student.id), index = True)
    has_taken : sqlo.Mapped[bool] = sqlo.mapped_column()
    been_sa : sqlo.Mapped[bool] = sqlo.mapped_column()
    grade : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(2))

    # relationships
    course : sqlo.Mapped[Course] = sqlo.relationship( back_populates= 'experiences')
    user : sqlo.Mapped[Student] = sqlo.relationship( back_populates= 'experiences')

=======
    term: sqlo.Mapped[str] = sqlo.mapped_column(primary_key=True)
    section: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    coursenum: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(4), primary_key=True)
>>>>>>> 928c89dddd649b3b19828b73614582caf17f7537


