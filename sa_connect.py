from config import Config

from app import create_app, db
from app.user.user_models import User, Student, Faculty
from app.course.course_models import Course
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo


app = create_app(Config)

preset_courses = [
    "CS1011 - Intro to Programming",
    "CS2303 - Algorithms",
    "CS3733 - Software Engineering",
    "CS4342 - Intro to AI"
]

@app.shell_context_processor
def make_shell_context():
    return {'sqla': sqla, 'sqlo': sqlo, 'db': db, 'User': User, 'Student': Student, 'Faculty': Faculty}

def add_courses(*args, **kwargs):
    query = sqla.select(Course)
    if db.session.scalars(query).first() is None:
        courses = [{'major':'CS','coursenum':'1101'},
          {'major':'DS','coursenum':'4432'},
          {'major':'RBE','coursenum':'2010'},
          {'major':'ME','coursenum':'2221'}, 
          {'major':'MA','coursenum': '3031'}  ]
        for c in courses:
            db.session.add(Course(major = c['major'], coursenum = c['coursenum']))
        db.session.commit()

@app.before_request
def init_db(*args, **kwargs):
    if app._got_first_request:
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)