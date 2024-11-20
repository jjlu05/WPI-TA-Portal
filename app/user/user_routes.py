from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user, login_user
from app import db
from app.user.user_forms import StudentRegistrationForm, FacultyRegistrationForm, CreateSAPositionForm
from app.user.user_models import User, Student, Faculty, CourseSection, SAPosition
from app.user import user_blueprint as bp_user


@bp_user.route('/', methods=['GET', 'POST'])
@bp_user.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@bp_user.route('/student/register', methods=['GET', 'POST'])
def register_student():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        # Create a new User object
        new_user = Student(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone_number=form.phone_number.data,
            wpi_id=form.wpi_id.data,
            major=form.major.data,
            grad_year=form.graduation_year.data,
            cum_gpa=form.gpa.data
        )
        # Set the password using the set_password method
        new_user.set_password(form.password.data)
    
        # Add the new user to the session and commit
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('user.login'))  # Assuming you have a 'login' route
        
    return render_template('register_student.html', form=form)

@bp_user.route('/faculty/register', methods=['GET', 'POST'])
def register_faculty():
    form = FacultyRegistrationForm()
    if form.validate_on_submit():
        # Create a new User object
        new_user = Faculty(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone_number=form.phone_number.data,
            wpi_id=form.wpi_id.data,
            department=form.department.data
        )
        # Set the password using the set_password method
        new_user.set_password(form.password.data)

        # Add the new user to the session and commit
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('user.login'))  # Assuming you have a 'login' route
        
    return render_template('register_faculty.html', form=form)

# Login route (no functionality yet, just placeholder)
@bp_user.route('/login', methods=['GET', 'POST'])
def login():
    """User login route """
    # Placeholder route for login - no functionality yet
    return render_template('login.html')


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