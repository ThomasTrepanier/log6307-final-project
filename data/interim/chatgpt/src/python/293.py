from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['GET', 'POST'])
def example_route():
    if request.method == 'GET':
        # Handle GET request
        return "This is a GET request"
    elif request.method == 'POST':
        # Handle POST request
        return "This is a POST request"

if __name__ == '__main__':
    app.run()
