import sys
from flask import render_template, flash, redirect, url_for, request, jsonify
import sqlalchemy as sqla

from app import db
from flask_login import current_user, login_required

from app.course import course_blueprint as bp_course

@bp_course.route('/', methods=['GET'])
@bp_course.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title="Smile Portal")