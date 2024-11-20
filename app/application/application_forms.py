from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SelectField, SubmitField, ValidationError
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email, Optional
from app.user.user_models import User, Student, Faculty

class CreateSAPositionForm(FlaskForm):
    course_section = SelectField('Course Section', choices=[], validators=[DataRequired()])
    number_of_sas = IntegerField('Number of SAs', validators=[DataRequired(), NumberRange(min=1)])
    qualifications = TextAreaField('Qualifications', validators=[DataRequired()])
    submit = SubmitField('Create SA Position')
