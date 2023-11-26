from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/get_webpage')
def get_webpage():
    target_url = request.args.get('url')
    if not target_url:
        return "No target URL provided."

    try:
        response = requests.get(target_url)
        if response.status_code == 200:
            return Response(response.content, content_type=response.headers['Content-Type'])
        else:
            return f"Failed to fetch content from {target_url}."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
