@app.route('/upload', methods=['POST'])
def urljson():
    json_data = request.get_json()
    url = json_data['url']
    download.download_func(url)
    crawler.crawler()
    prompt.prompt_work("output_1.txt")

    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
