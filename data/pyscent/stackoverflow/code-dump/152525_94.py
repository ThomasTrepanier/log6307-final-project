import json
@app.route("/")
def result():
  return render_template("result.html")

@app.route('/get_data')
def get_data():
  labels = ["Africa", "Asia", "Europe", "Latin America", "North America"]
  data = [5578,5267,734,784,433]
  return flask.jsonify({'payload':json.dumps({'data':data, 'labels':labels})})
