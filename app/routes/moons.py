from app import db
from app.models.moon_model import Moon
from flask import Blueprint, jsonify, make_response, request, abort


moons_bp = Blueprint("moons", __name__, url_prefix='/moons')
