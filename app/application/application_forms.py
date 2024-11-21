from flask_wtf import FlaskForm
from wtforms import BooleanField, FloatField, IntegerField, TextAreaField, SelectField, SubmitField, ValidationError
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email, Optional
from app.user.user_models import User, Student, Faculty

class CreateSAPositionForm(FlaskForm):
    course_section = SelectField('Course Section', choices=[], validators=[DataRequired()])
    number_of_sas = IntegerField('Number of SAs', validators=[DataRequired(), NumberRange(min=1)])
    min_gpa = FloatField('Minimum GPA', validators=[DataRequired(), NumberRange(min=0.0, max=4.0)])
    min_grade = StringField('Minimum Grade Earned (e.g., A, B+)', validators=[DataRequired()])
    prior_experience = BooleanField('Requires Prior SA Experience')
    
    submit = SubmitField('Create SA Position')
