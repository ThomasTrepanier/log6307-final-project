# use livereload==2.5.1 only
from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)
app.debug = True

@app.get("/")
def index():
    return render_template("index.html")

# don't use flask run, use python3 app.py
server = Server(app.wsgi_app)
server.watch("templates/*.*")  # or what have you
server.serve(port=5000) # if you want the standard Flask port
