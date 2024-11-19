from flask import render_template, redirect, url_for, flash
from app.user.user_forms import CreateSAPositionForm
from app.user.user_models import db, CourseSection, SAPosition
from app.user import user_blueprint as user

@user.route('/faculty/create', methods=['GET', 'POST'])
@login_required
def create_sa_position():
    if not current_user.faculty_profile:
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('index'))

    form = CreateSAPositionForm()

    # Populate the course section dropdown
    course_sections = CourseSection.query.filter_by(instructor_id=current_user.faculty_profile.id).all()
    form.course_section.choices = [(str(section.id), f"{section.course_code} - {section.section_number}") for section in course_sections]

    if form.validate_on_submit():
        sa_position = SAPosition(
            course_section_id=form.course_section.data,
            number_of_sas=form.number_of_sas.data,
            qualifications=form.qualifications.data,
        )
        db.session.add(sa_position)
        db.session.commit()
        flash('SA Position created successfully!', 'success')
        return redirect(url_for('faculty_page')) #fix this Url path for faculty page

    return render_template('faculty/create.html', form=form)
