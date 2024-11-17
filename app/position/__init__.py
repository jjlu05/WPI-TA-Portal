from flask import Blueprint

error_blueprint = Blueprint('position', __name__)

from app.errors import errors