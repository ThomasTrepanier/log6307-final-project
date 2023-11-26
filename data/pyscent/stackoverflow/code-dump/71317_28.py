from flask import Flask

app = Flask(__name__)

@app.route('/')
def about():
    return 'It worked!'

if __name__ == '__main__':
    app.run(host='192.168.43.81', port=5000, debug=True, threaded=False)