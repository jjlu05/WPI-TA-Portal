from app import db
from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SelectField, SubmitField, ValidationError
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, PasswordField, SubmitField, IntegerField, RadioField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, EqualTo, Email, Optional
from app.user.user_models import User, Student, Faculty
from app.course.course_models import Course
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

class CreateCourseForm(FlaskForm):
    section_number = IntegerField('Section', validators=[DataRequired()])
    term = StringField('Term', validators=[DataRequired()])
    submit = SubmitField('Create')
    course_choices = QuerySelectField(
        "Courses",
        query_factory=lambda: db.session.query(Course).order_by(Course.major, Course.coursenum).all(), 
        get_label=lambda course: f"{course.major} {course.coursenum}",
    )
