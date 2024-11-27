from flask_wtf import FlaskForm

from wtforms import FloatField, StringField, PasswordField, SubmitField, IntegerField, RadioField, BooleanField, TextAreaField, SelectField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Email, Optional, Length
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
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    courses_served = QuerySelectMultipleField(
        "Courses Served as SA",
        query_factory=lambda: db.session.query(Course).order_by(Course.major, Course.coursenum).all(), 
        get_label=lambda course: f"{course.major} {course.coursenum}", 
        widget=ListWidget(prefix_label=False), 
        option_widget=CheckboxInput(),  
    )
    courses_taken = QuerySelectMultipleField(
        "Courses Taken",
        query_factory=lambda: db.session.query(Course).order_by(Course.major, Course.coursenum).all(), 
        get_label=lambda course: f"{course.major} {course.coursenum}", 
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
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])

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

class StudentEditProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    major = StringField('Major', validators=[DataRequired()])
    cum_gpa = FloatField('Cumulative GPA', validators=[DataRequired()])
    grad_year = IntegerField('Graduation Year', validators=[DataRequired()])
    courses_served = QuerySelectMultipleField(
        "Courses Served as SA",
        query_factory=lambda: db.session.query(Course).order_by(Course.major, Course.coursenum).all(), 
        get_label=lambda course: f"{course.major} {course.coursenum}", 
        widget=ListWidget(prefix_label=False), 
        option_widget=CheckboxInput(),  
    )
    courses_taken = QuerySelectMultipleField(
        "Courses Taken",
        query_factory=lambda: db.session.query(Course).order_by(Course.major, Course.coursenum).all(), 
        get_label=lambda course: f"{course.major} {course.coursenum}", 
        widget=ListWidget(prefix_label=False), 
        option_widget=CheckboxInput(),  
    )
    submit = SubmitField('Update Profile')


class FacultyEditProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    department = StringField('Department', validators=[DataRequired()])
    submit = SubmitField('Update Profile')