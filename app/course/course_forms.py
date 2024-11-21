from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SelectField, SubmitField, ValidationError
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, PasswordField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, EqualTo, Email, Optional
from app.user.user_models import User, Student, Faculty

class CreateCourseForm(FlaskForm):
    section_number = IntegerField('Section', validators=[DataRequired()])
    term = StringField('Term', validators=[DataRequired()])
    submit = SubmitField('Create')
    course_choices = [("test1", "CS3733"), ("test2", "CS3431"), ("test3", "HI4100"), ("test2", "CS3431"), ("test3", "HI4100"), ("test2", "CS3431"), ("test3", "HI4100"), ("test2", "CS3431"), ("test3", "HI4100"), ("test2", "CS3431"), ("test3", "HI4100")]

    major = RadioField('Major', choices=course_choices, validators=[DataRequired()])
