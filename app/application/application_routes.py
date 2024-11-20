from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user, login_user
from app import db
from app.application.application_forms import CreateSAPositionForm
from app.application.application_models import SAPosition
from app.user.user_models import Faculty
from app.user import user_blueprint as bp_user
from app.course.course_models import CourseSection




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
        (str(section.id), f"{section.course_code} - {section.section_number}") 
        for section in course_sections
    ]

    if form.validate_on_submit():
        sa_position = SAPosition(
            course_section_id=int(form.course_section.data),  # Ensure integer type
            number_of_sas=form.number_of_sas.data,
            qualifications=form.qualifications.data,
        )
        db.session.add(sa_position)
        db.session.commit()
        flash('SA Position created successfully!', 'success')
        return redirect(url_for('user.faculty_page'))  # fix to reflect faculty main page 

    return render_template('create.html', form=form)