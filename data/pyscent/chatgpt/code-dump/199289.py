from flask import Flask, jsonify, request
import crawler
import download
import prompt
import json

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def urljson():
    url = request.get_json()
    download.download_func(url['url'])
    crawler.crawler()
    response = prompt.prompt_work("output_1.txt")
    print("response is going")
    return jsonify({"response": str(response)})

if __name__ == '__main__':
    app.run(debug=True)
