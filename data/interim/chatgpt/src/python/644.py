from flask import Blueprint, request, jsonify
from .envapi import validation, database

locations_blueprint = Blueprint('locations', __name__)

@locations_blueprint.route('/locations', methods=['POST'])
def create_location():
    is_valid, error = validation.validate_location(request)
    if not is_valid:
        return jsonify({"error": error}), 400
    try:
        new_location = {...}
        location_id = database.locations.add(new_location)
        return jsonify(new_location), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
