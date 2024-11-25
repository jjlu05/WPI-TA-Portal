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

class ApplyForSAPosition(FlaskForm):
    test = IntegerField()
    grade = SelectField('Grade Earned', choices=[], validators=[DataRequired()])
    year_term_course = StringField('Year and term you took the course(i.e "2023B" or "N/A")', validators=[DataRequired()])
    year_term_apply = StringField('Year and term you are applying for SAship', validators=[DataRequired()])
    submit = SubmitField('Apply For SA Position')
