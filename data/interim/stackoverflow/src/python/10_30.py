from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/math/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return '%d' % (num1+num2)
