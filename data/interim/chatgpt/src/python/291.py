from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/example')
def example_route():
    # Perform some logic
    if condition:
        return jsonify({'message': 'Success'}), 200  # Return 200 OK status code
    else:
        return jsonify({'message': 'Error'}), 500  # Return 500 Internal Server Error status code

if __name__ == '__main__':
    app.run()
