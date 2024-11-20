from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, IntegerField, RadioField, BooleanField, TextAreaField, SelectField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Email, Optional
from app.user.user_models import User, Student, Faculty
from app.course.course_models import Course

from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

from app import db


class StudentRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match.")])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    major = StringField('Major', validators=[DataRequired()])
    gpa = IntegerField('GPA (Optional)', validators=[Optional()])
    graduation_year = IntegerField('Graduation Year', validators=[DataRequired()])
    wpi_id = StringField('WPI ID', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    past_sa = StringField('Past SA')

    courses_served = QuerySelectMultipleField(
        "Courses Served as SA",
        query_factory=lambda: db.session.query(Course).all(), 
        get_label=lambda course: course.name, 
        widget=ListWidget(prefix_label=False), 
        option_widget=CheckboxInput(),  
    )
    
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Student.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different username.')
        user = Faculty.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different username.')

    def validate_email(self, email):
        user = Student.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered. Please use a different email address.')
        user = Faculty.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered. Please use a different email address.')


class FacultyRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match.")])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    wpi_id = StringField('WPI ID', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])

    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Student.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different username.')
        user = Faculty.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different username.')

    def validate_email(self, email):
        user = Student.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered. Please use a different email address.')
        user = Faculty.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered. Please use a different email address.')
        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')

class CreateCourseForm(FlaskForm):
    section_number = IntegerField('Section', validators=[DataRequired()])
    term = StringField('Term', validators=[DataRequired()])
    submit = SubmitField('Create')
    course_choices = [("test1", "CS3733"), ("test2", "CS3431"), ("test3", "HI4100"), ("test2", "CS3431"), ("test3", "HI4100"), ("test2", "CS3431"), ("test3", "HI4100"), ("test2", "CS3431"), ("test3", "HI4100"), ("test2", "CS3431"), ("test3", "HI4100")]
    major = RadioField('Major', choices=course_choices, validators=[DataRequired()])

    
