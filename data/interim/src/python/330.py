from flask import Flask, request

app = Flask(__name__)

@app.route('/example')
def example_route():
    # Accessing a specific header
    user_agent = request.headers.get('User-Agent')
    print(f"User-Agent: {user_agent}")

    # Accessing all headers
    headers = dict(request.headers)
    print(headers)

    # Do further processing with the headers

    return "Request Headers Example"

if __name__ == '__main__':
    app.run()
