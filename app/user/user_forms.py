from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class CreateSAPositionForm(FlaskForm):
    course_section = SelectField('Course Section', choices=[], validators=[DataRequired()])
    number_of_sas = IntegerField('Number of SAs', validators=[DataRequired(), NumberRange(min=1)])
    qualifications = TextAreaField('Qualifications', validators=[DataRequired()])
    submit = SubmitField('Create SA Position')
