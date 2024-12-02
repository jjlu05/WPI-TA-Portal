from app import db
from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SelectField, SubmitField, ValidationError
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, PasswordField, SubmitField, IntegerField, RadioField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, EqualTo, Email, Optional, Length
from app.user.user_models import User, Student, Faculty
from app.course.course_models import Course, CourseSection
from app.static import form_options
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from sqlalchemy import cast, Integer
 
def is_numeric(form, field):
    if not field.data.isdigit():
        raise ValidationError('Field can only contain numeric characters.')


class CreateCourseForm(FlaskForm):
    section_number = StringField('Section (Optional: Section number will be auto-assigned if left empty)', 
                                 validators=[Optional(), Length(min=0, max=3), is_numeric])
    term = SelectField("Term", choices=form_options.future_class_terms)
    submit = SubmitField('Create')

    course_choices = QuerySelectField(
        "Courses",
        query_factory=lambda: db.session.query(Course).order_by(Course.major, Course.coursenum).all(),
        get_label=lambda course: f"{course.major} {course.coursenum}",
    )

    def validate_section_number(self, section_number):
        if section_number.data:
            try:
                section_number_int = int(section_number.data)
            except ValueError:
                raise ValidationError('Section number must be a valid integer.')
            
            if section_number_int < 1 or section_number_int > 999:
                raise ValidationError('Section number must be between 1 and 999.')
            
            course_offering = CourseSection.query.filter_by(
                section_number=section_number_int, 
                term=self.term.data, 
                course=self.course_choices.data
            ).first()

            if course_offering:
                raise ValidationError('Course with the same section number already exists in this term.')