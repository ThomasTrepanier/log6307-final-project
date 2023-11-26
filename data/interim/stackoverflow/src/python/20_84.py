@app.route("/predict", methods=["POST"])
def predict():

    if flask.request.method == "POST":

            output=model.predict(data)  #what you want to do with frozen model goes here
