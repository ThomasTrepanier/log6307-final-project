@app.route('/locations', methods=['POST'])  
def create_location():
    ...

locations_blueprint = Blueprint('locations', __name__)

@locations_blueprint.route('/locations', methods=['POST'])
def create_location(): 
    ...
app.register_blueprint(locations_blueprint)
