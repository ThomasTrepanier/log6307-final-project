from flask import Flask, render_template

app = FLASK(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/')
def about():
    return render_template('about.html')
