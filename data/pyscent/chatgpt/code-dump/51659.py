from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return 'Hello, Flask Server!'

# Define another route
@app.route('/about')
def about():
    return 'This is the about page.'

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
