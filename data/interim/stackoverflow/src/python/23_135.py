@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        user=request.form["nm"]
    else:
        user=request.args.get("nm")
    if user:
        return redirect(url_for('success', name = str(user)))
    else:
        return "go to the form"
