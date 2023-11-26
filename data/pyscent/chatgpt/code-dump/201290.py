from flask import Flask, jsonify, request
import crawler
import download
import prompt
import json

app = Flask(__name__)

class prompt_work():
    # ... existing code ...

    def get_response(self):
        # ... logic to obtain the response ...
        return response

@app.route('/upload', methods=['POST'])
def urljson():
    url = request.get_json()
    download.download_func(url['url'])
    crawler.crawler()
    
    pw = prompt.prompt_work("output_1.txt")
    response = pw.get_response()
    
    print("response is going")
    return jsonify({"response": str(response)})

if __name__ == '__main__':
    app.run(debug=True)
