from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class CreateSAPositionForm(FlaskForm):
    course_section = SelectField('Course Section', choices=[], validators=[DataRequired()])
    number_of_sas = IntegerField('Number of SAs', validators=[DataRequired(), NumberRange(min=1)])
    qualifications = TextAreaField('Qualifications', validators=[DataRequired()])
    submit = SubmitField('Create SA Position')
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email, Optional
from app.user.user_models import User, Student, Faculty

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
    
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
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
    faculty_id = StringField('Faculty ID', validators=[DataRequired()])
    
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered. Please use a different email address.')
