from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user, login_user
from app import db
from app.application.application_forms import CreateSAPositionForm, ApplyForSAPosition
from app.application.application_models import SAPosition, SAApplication
from app.user.user_models import Faculty
from app.user import user_blueprint as bp_user
from app.course.course_models import CourseSection
from datetime import date




@bp_user.route('/faculty/create', methods=['GET', 'POST'])
@login_required
def create_sa_position():
    # Check if the current user is a Faculty member
    if not isinstance(current_user, Faculty):
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('user.index'))

    form = CreateSAPositionForm()

    # Populate the course section dropdown
    course_sections = CourseSection.query.filter_by(instructor_id= Faculty.id).all()
    form.course_section.choices = [
        (str(section.id), f"{section.course.major} {section.course.coursenum} - {section.section_number}") 
        for section in course_sections
    ]

    if form.validate_on_submit():
        sa_position = SAPosition(
            course_section_id=form.course_section.data,
            number_of_sas=form.number_of_sas.data,
            min_gpa=form.min_gpa.data,
            min_grade=form.min_grade.data,
            prior_experience=form.prior_experience.data,
            current_date = date.today()
        )
        db.session.add(sa_position)
        db.session.commit()
        flash('SA Position created successfully!', 'success')
        return redirect(url_for('user.index'))  # fix to reflect faculty main page 

    return render_template('create.html', form=form, is_faculty=True)







@bp_user.route('/student/apply/<int:pos_id>', methods=['GET', 'POST'])
@login_required
def apply(pos_id):
    # Check if the current user is a Faculty member
    if isinstance(current_user, Faculty):
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('user.index'))

    form = ApplyForSAPosition()
    form.test.data = pos_id
    pos = SAPosition.query.get(pos_id)  

    form.grade.choices=['A','B','C']
    if form.validate_on_submit():
        sa_Application = SAApplication(
            student_id = current_user.id,
            position_id = form.test.data,
            grade=form.grade.data,
            year_term_course = form.year_term_course.data,
            year_term_apply = form.year_term_apply.data
        )
        db.session.add(sa_Application)
        db.session.commit()
        flash('SA Application successful!', 'success')
        return redirect(url_for('user.index'))  

    return render_template('applicationForm.html', form=form, pos=pos)


@bp_user.route('/faculty/view_applications/<int:pos_id>', methods=['GET'])
@login_required
def view_applications(pos_id):
    # Ensure only faculty can access this page
    if not isinstance(current_user, Faculty):
        flash("Access denied: Only faculty members can view applications.", "danger")
        return redirect(url_for('user.index'))

    # Fetch the position and associated applications
    sa_position = SAPosition.query.get_or_404(pos_id)

    # Check if the current user is the instructor for the position
    if sa_position.course_section.instructor_id != current_user.id:
        flash("Access denied: You do not manage this position.", "danger")
        return redirect(url_for('user.index'))

    # Retrieve applications
    applications = sa_position.applications

    return render_template(
        'view_applications.html',
        sa_position=sa_position,
        applications=applications
    )
