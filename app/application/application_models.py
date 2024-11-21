from app import db, login
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from app.course.course_models import CourseSection

 
 
 
#SA Position Model
class SAPosition(db.Model):
    __tablename__ = 'sa_position'  # Explicitly defines the table name
    
    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    course_section_id: sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey('course_section.id'), nullable=False)
    number_of_sas: sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer, nullable=False)
    min_gpa: sqlo.Mapped[float] = sqlo.mapped_column(sqla.Float, nullable=False, default=0.0)  
    min_grade: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(2), nullable=False, default="C")  
    prior_experience: sqlo.Mapped[bool] = sqlo.mapped_column(sqla.Boolean, nullable=False, default=False)  

    # Relationship
    course_section: sqlo.Mapped['CourseSection'] = sqlo.relationship('CourseSection', back_populates='sa_positions')

    def __repr__(self):
        return (
            f"<SAPosition(id={self.id}, course_section_id={self.course_section_id}, "
            f"number_of_sas={self.number_of_sas}, min_gpa={self.min_gpa}, "
            f"min_grade='{self.min_grade}', prior_experience={self.prior_experience})>"
        )