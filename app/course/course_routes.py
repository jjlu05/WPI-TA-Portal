import sys
from flask import render_template, flash, redirect, url_for, request, jsonify
import sqlalchemy as sqla

from app import db
from flask_login import current_user, login_required

from app.course import course_blueprint as bp_course
from app import db
from app.user.user_forms import CreateCourseForm
from app.user.user_models import Course



@bp_course.route('/', methods=['GET'])
@bp_course.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title="Smile Portal")

@bp_course.route('/coursecreate', methods=['GET', 'POST'])
def createclass():
    cform = CreateCourseForm()
    if cform.validate_on_submit():
        new_class = Course(
            coursenum=cform.coursenum.data,
            section=cform.section.data,
            term=cform.term.data
            )
        db.session.add(new_class)
        db.session.commit()
        flash('Course "' + new_class.coursenum + '" is created')
        return redirect(url_for('course.index'))
    return render_template('addcourse.html', form=cform)
