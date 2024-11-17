from flask import Blueprint

error_blueprint = Blueprint('application', __name__)

from app.errors import errors

###