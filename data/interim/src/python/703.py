# Location creation endpoint 
@app.route('/locations', methods=['POST']) 
def create_location():
    try:
        # Validate request payload
        valid, errors = validate_create(request, "locations")
        if not valid:
            return jsonify({"errors": errors}), 400 

        # Check for missing description and return prompt if needed
        
        # Add new location to collection 
        new_location = {...}
        location_id = locations.add(new_location)

        # Update connected locations to reference new location ID  

        return jsonify(new_location), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
