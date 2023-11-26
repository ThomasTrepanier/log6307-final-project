@app.route("/test", methods=['GET','POST'])
def check():
    arr.append(request.form['a'])
    arr.append(request.form['b'])
    res = {'Status': True}
    app.csvwriter.send(arr)
    return json.dumps(res)
