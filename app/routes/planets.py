from app import db
from app.models.planet_model import Planet
from flask import Blueprint, jsonify, make_response, request, abort


planets_bp = Blueprint("planets", __name__, url_prefix='/planets')


@planets_bp.route('', methods=['GET'])
def get_all_planets():
    name_query = request.args.get('name')
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    planet_response = []
    for planet in planets:
        planet_response.append({
                "id": planet.id, 
                "name": planet.name,
                "description": planet.description, 
                "mass": planet.mass
        })
    return jsonify(planet_response)

@planets_bp.route('', methods=['POST'])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body['name'], description=request_body['description'], mass=request_body['mass'])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({'message': f'{id} is invalid'}, 400))
    
    planet = Planet.query.get(id)
    if not planet:
        abort(make_response({"message": f"planet {id} not found"}, 404))
    return planet


@planets_bp.route('/<id>', methods=['GET'])
def get_one_planet(id):
    planet = validate_planet(id)
    return {"id": planet.id, "name": planet.name,
            "description": planet.description, "mass": planet.mass}


@planets_bp.route('/<id>', methods=['PUT'])
def update_planet(id):
    planet = validate_planet(id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.mass = request_body["mass"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")


@planets_bp.route('/<id>', methods=['DELETE'])
def delete_planet(id):
    planet = validate_planet(id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f'Planet #{id} successfully deleted')
