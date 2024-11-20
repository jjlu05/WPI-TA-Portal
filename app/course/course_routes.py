import sys
from flask import render_template, flash, redirect, url_for, request, jsonify
import sqlalchemy as sqla

from app import db
from flask_login import current_user, login_required

from app.course import course_blueprint as bp_course
from app import db
from app.course.course_forms import CreateCourseForm
from app.course.course_models import CourseSection
from app.user.user_models import Faculty




@bp_course.route('/', methods=['GET'])
@bp_course.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp_course.route('/course/create', methods=['GET', 'POST'])
@login_required
def createclass():
    if not isinstance(current_user, Faculty):
        flash('You do not have permission to create courses', 'danger')
        return redirect(url_for('user.index'))
    cform = CreateCourseForm()
    if cform.validate_on_submit():
        new_class = CourseSection(
            course_code=cform.major.data,
            section_number=cform.section_number.data,
            term=cform.term.data,
            instructor_id=1
            )
    
        db.session.add(new_class)
        db.session.commit()
        flash('Course "' + new_class.course_code + '" is created')
        return redirect(url_for('user.index'))
    print(cform.errors)
    return render_template('addcourse.html', form=cform)