from flask import jsonify, render_template, redirect, url_for, flash
from flask_login import login_required, current_user, login_user
from app import db
from app.application.application_forms import CreateSAPositionForm, ApplyForSAPosition
from app.application.application_models import SAPosition, SAApplication
from app.user.user_models import Faculty
from app.user import user_blueprint as bp_user
from app.course.course_models import CourseSection, Course, CourseExperience
from datetime import date, datetime
from datetime import timezone 
import datetime 
import sqlalchemy.orm as sqlo



@bp_user.route('/faculty/create', methods=['GET', 'POST'])
@login_required
def create_sa_position():
    # Check if the current user is a Faculty member
    if not isinstance(current_user, Faculty):
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('user.index'))

    form = CreateSAPositionForm()

    # Populate the course section dropdown
    course_sections = CourseSection.query.filter_by(instructor_id=current_user.id).join(CourseSection.course).order_by(Course.major, Course.coursenum, CourseSection.term, CourseSection.section_number).all()
    form.course_section.choices = [(str(section.id), f"{section.course.major} {section.course.coursenum} - {section.section_number} - {section.term}") for section in course_sections]

    if form.validate_on_submit():
        sa_position = SAPosition(
            course_section_id=form.course_section.data,
            number_of_sas=form.number_of_sas.data,
            min_gpa=form.min_gpa.data,
            min_grade=form.min_grade.data,
            prior_experience=form.prior_experience.data,
            current_date = datetime.datetime.now(timezone.utc).date()

        )
        db.session.add(sa_position)
        db.session.commit()
        flash('SA Position created successfully!', 'success')
        return redirect(url_for('user.index'))  # fix to reflect faculty main page 

    return render_template('create.html', form=form, is_faculty=True)




@bp_user.route('/student/apply/<int:pos_id>', methods=['GET', 'POST'])
@login_required
def apply(pos_id):
    if isinstance(current_user, Faculty):
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('user.index'))

    form = ApplyForSAPosition()
    pos = SAPosition.query.get_or_404(pos_id)

    existing_application = SAApplication.query.filter_by(student_id=current_user.id, position_id=pos_id).first()
    if existing_application:
        flash('You have already applied for this position.', 'warning')
        return redirect(url_for('user.index'))

    experience = db.session.query(CourseExperience).filter(
        CourseExperience.user == current_user,
        CourseExperience.course == pos.course_section.course
    ).first()

    term_course = 'None'
    course_grade = 'NA'
    if experience and experience.has_taken:
        term_course = experience.term_taken
        course_grade = experience.grade

    if form.validate_on_submit():
        sa_application = SAApplication(
            student=current_user,
            position_id=pos.id,
            grade=course_grade,
            year_term_course=term_course,
            year_term_apply=pos.course_section.term
        )
        db.session.add(sa_application)
        db.session.commit()
        flash('SA Application successful!', 'success')
        return redirect(url_for('user.index'))

    
    sa_experience = "Yes" if db.session.query(CourseExperience).filter(
        CourseExperience.user == current_user,
        CourseExperience.been_sa == True
    ).first() else "No"

    return render_template(
        'applicationForm.html',
        form=form,
        pos=pos,
        experience=experience,
        sa_experience=sa_experience
    )


@bp_user.route('/withdraw_application/<int:application_id>', methods=['POST'])

def withdraw_application(application_id):
    application = SAApplication.query.get(application_id)
    if not application:
        return jsonify({'status': 'error', 'message': 'Application not found'}), 404

    db.session.delete(application)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Application withdrawn successfully'}), 200


@bp_user.route('/faculty/view-applications/<int:pos_id>', methods=['GET'])
@login_required
def view_applications(pos_id):
    if not isinstance(current_user, Faculty):
        flash("Access denied: Only faculty members can view applications.", "danger")
        return redirect(url_for('user.index'))

    sa_position = SAPosition.query.get_or_404(pos_id)

    if sa_position.course_section.instructor_id != current_user.id:
        flash("Access denied: You do not manage this position.", "danger")
        return redirect(url_for('user.index'))

    applications = db.session.query(SAApplication).filter_by(position_id=pos_id).all()

    application_data = []
    for application in applications:
        is_already_hired = application.is_assigned
        application_data.append((application, is_already_hired))

    return render_template(
        'view_applications.html',
        sa_position=sa_position,
        applications=application_data,
        is_faculty=True
    )


@bp_user.route('/faculty/approve_application/<int:app_id>', methods=['POST'])
@login_required
def approve_application(app_id):
    if not isinstance(current_user, Faculty):
        flash("Access denied: Only faculty members can approve applications.", "danger")
        return redirect(url_for('user.index'))

    application = SAApplication.query.get_or_404(app_id)

    if application.saPosition.course_section.instructor_id != current_user.id:
        flash("Access denied: You do not manage this position.", "danger")
        return redirect(url_for('user.index'))

    assigned_count = db.session.query(SAApplication).filter(
        SAApplication.position_id == application.position_id,
        SAApplication.is_assigned == True
    ).count()

    if assigned_count >= application.saPosition.number_of_sas:
        flash("Cannot approve: Maximum number of SAs already assigned.", "danger")
        return redirect(url_for('user.view_applications', pos_id=application.position_id))

    
    application.is_assigned = True
    db.session.commit()
    flash("Application approved successfully!", "success")
    return redirect(url_for('user.view_applications', pos_id=application.position_id))

