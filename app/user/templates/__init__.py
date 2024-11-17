from flask import Blueprint

error_blueprint = Blueprint('user', __name__)

from app.errors import errors