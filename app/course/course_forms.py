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
    course_choices = [("CS3733", "CS3733"), ("CS3431", "CS3431"), ("HI4100", "HI4100"), ("RBE2000", "RBE2000"), ("HI1001", "HI1001"), ("BB2100", "BB2100"), ("CN3000", "CN3000")]
    major = RadioField('Major', choices=course_choices, validators=[DataRequired()])
