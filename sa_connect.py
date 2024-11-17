from config import Config

from app import create_app, db
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

app = create_app(Config)

@app.shell_context_processor
def make_shell_context():
    return {'sqla': sqla, 'sqlo': sqlo, 'db': db}

@app.before_request
def init_db(*args, **kwargs):
    if app._got_first_request:
        db.create_all()

app.run(debug=True)