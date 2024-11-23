import sys
from flask import render_template, flash, redirect, url_for, request, jsonify
from sqlalchemy import func
import sqlalchemy as sqla

from app import db
from flask_login import current_user, login_required

from app.course import course_blueprint as bp_course
from app import db
from app.course.course_forms import CreateCourseForm
from app.course.course_models import CourseSection, CourseExperience
from app.user.user_models import Faculty,Student
from app.course.course_models import Course
from app.application.application_models import SAPosition




@bp_course.route('/', methods=['GET'])
@bp_course.route('/index', methods=['GET', 'POST'])
def index():
    isStudent=False
    listOfRelevantPos= []
    facultyCourses = []
    SAPosCourses = []
    if isinstance(current_user, Student):
        isStudent=True
        studentCourses = db.session.scalars(sqla.select(CourseExperience.id).where(CourseExperience.has_taken == True)).all()
        SAPosCourses = db.session.scalars(sqla.select(SAPosition)).all()

        for c in studentCourses:
            for SAPos in SAPosCourses:
                if c==SAPos.course_section_id.course_id:#still need course and course section relationship
                    listOfRelevantPos.append(SAPos)
                    SAPosCourses.remove(SAPos)

    
    if isinstance(current_user, Faculty):
        facultyCourses = db.session.execute(sqla.select(CourseSection).where(CourseSection.instructor_id==current_user.id)).scalars().all()


    return render_template('index.html',facultyCourses = facultyCourses, current_user=current_user, isStudent =isinstance(current_user, Student), is_faculty=isinstance(current_user, Faculty), listOfRelevantPos = listOfRelevantPos, SAPosCourses = SAPosCourses)

@bp_course.route('/course/create', methods=['GET', 'POST'])
@login_required
def createclass():
    faculty_member = Faculty.query.filter_by(id=current_user.id).first()

    if not isinstance(current_user, Faculty):
        flash('You do not have permission to create courses', 'danger')
        return redirect(url_for('user.index'))
    cform = CreateCourseForm()
    if cform.validate_on_submit():
        new_class = CourseSection(
            course_code=cform.major.data,
            section_number=cform.section_number.data,
            term=cform.term.data,
            instructor_id=current_user.id)
            #course_id = db.session.scalars(sqla.select(Course.id).where(func.substring(cform.major.data, 2, 5) == Course.id)).first())
        
    
        db.session.add(new_class)
        db.session.commit()
        flash('Course "' + new_class.course_code + '" is created')
        return redirect(url_for('user.index'))
    print(cform.errors)
    return render_template('addcourse.html', form=cform)