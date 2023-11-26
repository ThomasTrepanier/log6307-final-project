from flask import Flask, flash, request, redirect, url_for, session
import json

app = Flask(__name__)

@app.route("/test", methods=['GET','POST'])
def check():
    arr = []
    arr.append(request.form['a'])
    arr.append(request.form['b'])
    res = {'Status': True}

    @flask.after_this_request
    def add_close_action(response):
        @response.call_on_close
        def process_after_request():
            df = pd.DataFrame({'x': arr})
            df.to_csv("docs/xyz.csv", index=False)
        return response
    return json.dumps(res)
