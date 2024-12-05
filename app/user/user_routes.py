from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from app import db
from app.user.user_forms import FacultyEditProfileForm, StudentEditProfileForm, StudentRegistrationForm, FacultyRegistrationForm, LoginForm
from app.user.user_models import User, Student, Faculty
from app.course.course_models import CourseExperience, CourseSection
from app.application.application_models import SAPosition
from app.course.course_models import Course, CourseExperience
from app.user import user_blueprint as bp_user
import sqlalchemy as sqla

@bp_user.route('/', methods=['GET', 'POST'])
@bp_user.route('/index', methods=['GET', 'POST'])
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
        # Retrieve courses and sections managed by the faculty
        facultyCourses = db.session.scalars(
            sqla.select(CourseSection).where(CourseSection.instructor_id == current_user.id)).all()

        # Get IDs of the faculty's course sections
        faculty_section_ids = [section.id for section in facultyCourses]

        # Fetch SA positions associated with these course sections
        SAPosCourses = db.session.scalars(sqla.select(SAPosition).where(SAPosition.course_section_id.in_(faculty_section_ids))).all()

        return render_template(
                                'index.html',
                                facultyCourses=facultyCourses,
                                current_user=current_user,
                                isStudent=isStudent,
                                is_faculty=isinstance(current_user, Faculty),
                                listOfRelevantPos=listOfRelevantPos,
                                SAPosCourses=SAPosCourses
                            )

@bp_user.route('/student/register', methods=['GET', 'POST'])
def register_student():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        print("Form submitted and validated")

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
            cum_gpa=form.gpa.data,
        )
        # Set the password using the set_password method
        new_user.set_password(form.password.data)

        # Add the new user to the session
        db.session.add(new_user)

        # Create experience table for student
        courses = db.session.scalars(sqla.select(Course)).all()
        for c in courses:
            db.session.add(CourseExperience(course_id = c.id, user_id = new_user.id))
        db.session.commit()

        # Record the courses the user selected
        for c in form.courses_served.data:
            experience = CourseExperience.query.filter_by(course = c, user = new_user).first()
            experience.been_sa = True
        for c in form.courses_taken.data:
            experience = CourseExperience.query.filter_by(course = c, user = new_user).first()
            experience.has_taken = True
        db.session.commit()


        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('user.login'))  
    else:
        print("Form validation failed")
        
    return render_template('register_student.html', form=form)
    

@bp_user.route('/faculty/register', methods=['GET', 'POST'])
def register_faculty():
    if current_user.is_authenticated:
        return redirect(url_for('user.index'))

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
        return redirect(url_for('user.login'))  
        
    return render_template('register_faculty.html', form=form)


@bp_user.route('/login', methods=['GET', 'POST'])
def login():
    # If the user is already logged in, redirect to the index page
    if current_user.is_authenticated:
        return redirect(url_for('course.index'))

    form = LoginForm()
    
    if form.validate_on_submit():
        # Check for the user in both Student and Faculty tables
        query = sqla.select(Student).where(Student.username == form.username.data)
        user = db.session.scalars(query).first()       
        if user is None:
            query = sqla.select(Faculty).where(Faculty.username == form.username.data)
            user = db.session.scalars(query).first()
        if (user is None) or (user.check_password(form.password.data) == False):
            flash('Incorrect username or password.')
            return redirect(url_for('user.login'))
        login_user(user, remember = form.remember_me.data)
        flash('Welcome back, {}!'.format(current_user.username))
        return redirect(url_for('user.index'))
    return render_template('login.html', form=form)

@bp_user.route('/logout', methods=['GET'])
@login_required 
def logout():
    logout_user()  
    flash('You have been logged out.', 'info')
    return redirect(url_for('user.index')) 


@bp_user.route('/student/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_student_profile():
    if not isinstance(current_user, Student):
        flash("Unauthorized access", "danger")
        return redirect(url_for('user.index'))
    
    form = StudentEditProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        current_user.phone_number = form.phone_number.data
        current_user.major = form.major.data
        current_user.cum_gpa = form.cum_gpa.data
        current_user.grad_year = form.grad_year.data

        db.session.commit()
        flash('Student profile updated successfully!')
        return redirect(url_for('user.edit_student_profile'))
    
    return render_template('edit_student_profile.html', form=form, courses=db.session
                           .query(CourseExperience).filter(CourseExperience.user == current_user, sqla.or_(CourseExperience.has_taken, CourseExperience.been_sa))
                           .join(CourseSection.course).order_by(CourseExperience.been_sa.desc(), CourseExperience.has_taken, Course.major, Course.coursenum).all())

# Faculty Edit Profile
@bp_user.route('/faculty/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_faculty_profile():
    if not isinstance(current_user, Faculty):
        flash("Unauthorized access")
        return redirect(url_for('user.index'))
    
    form = FacultyEditProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        current_user.phone_number = form.phone_number.data
        current_user.department = form.department.data
        db.session.commit()
        flash('Faculty profile updated successfully!')
        return redirect(url_for('user.edit_faculty_profile'))
    
    return render_template('edit_faculty_profile.html', form=form, is_faculty=True)