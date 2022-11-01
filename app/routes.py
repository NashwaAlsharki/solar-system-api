from app import db
from app.models.planets import Planet
from flask import Blueprint, jsonify, make_response, request


planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')


@planets_bp.route('', methods=['POST'])
def get_all_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body['name'],
                        description=request_body['description'],
                        mass=request_body['mass'])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


# @planets_bp.route('/<id>', methods=['GET'])
# def validate_planet(id):
#     try:
#         id = int(id)
#     except ValueError:
#         return {"message": f"planet {id} invalid"}, 400

#     for planet in planet_list:
#         if planet.id == id:
#             return vars(planet)

    return {"message": f"planet {id} not found"}, 404


def get_one_planet(id):
    planet = validate_planet(id)
    return planet
