from flask import Blueprint

position_blueprint = Blueprint('position', __name__)

from app.position import position_routes