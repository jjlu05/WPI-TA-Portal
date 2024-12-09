from app import db
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from app.user.user_models import Student
from app.application.application_models import SAPosition
from app.course.course_models import CourseExperience

def get_weight(student, sa_position):
    if not meets_requirements(student, sa_position):
        return 0

    weight = 0
    experience = CourseExperience.query.filter_by(course = sa_position.course_section.course, user = student).first()
    if experience.has_taken:
        weight += 10

    if experience.been_sa:
        weight += 20

    return weight

def meets_requirements(student, sa_position):
    if student.cum_gpa <= sa_position.min_gpa - 0.00001: # account for float variance
        return False
    experience = CourseExperience.query.filter_by(course = sa_position.course_section.course, user = student).first()
    
    return True