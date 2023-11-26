@app.route('/result', methods=['POST', 'GET'])
def res_json():
    if request.method == "POST":
        text = request.form.get('query')
        payload = {"sender": "Rasa", "text": text}
        headers = {'content-type': 'application/json'}
        response = requests.post('http://localhost:5005/model/parse', json=payload, headers=headers)
        result = response.json()
        return result
