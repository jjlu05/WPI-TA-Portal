from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user, login_user
from app import db
from app.user.user_forms import StudentRegistrationForm, FacultyRegistrationForm, LoginForm
from app.user.user_models import User, Student, Faculty
from app.user import user_blueprint as bp_user
import sqlalchemy as sqla


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


@bp_user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('course.index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Check for user from both student and faculty
        query = sqla.select(Student).where(Student.username == form.username.data)
        user = db.session.scalars(query).first()
        if (user is None):
            query = sqla.select(Faculty).where(Faculty.username == form.username.data)
            user = db.session.scalars(query).first()
        if (user is None) or (user.check_password(form.password.data) == False):
            flash('Incorrect username or password.')
            return redirect(url_for('user.login'))
        login_user(user, remember = form.remember_me.data)
        flash('Welcome back, {}!'.format(current_user.username))
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)


