from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user, login_user
from app import db
from app.user.user_forms import StudentRegistrationForm, FacultyRegistrationForm
from app.user.user_models import User, Student, Faculty
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
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone_number=form.phone_number.data
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
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone_number=form.phone_number.data
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
    """User login route (you need to implement the form and authentication logic)."""
    # Placeholder route for login - no functionality yet
    return render_template('login.html')
