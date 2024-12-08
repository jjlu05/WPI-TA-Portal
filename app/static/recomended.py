from app import db
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from app.user.user_models import Student
from app.application.application_models import SAPosition
from app.course.course_models import CourseExperience

def get_weight(student, sa_position):
    experience = CourseExperience.query.filter_by(course = sa_position.course_section.course, user = student).first()
    weight = 0

    if experience.has_taken:
        weight += 10

    if experience.been_sa:
        weight += 20

    return weight