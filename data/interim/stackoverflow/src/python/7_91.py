def func1():
    print("Print function executed1")
    time.sleep(10)
    print("Print function executed2")

app = Flask(__name__)

@app.route("/first")
def main():
    print("Request received1")
    func1()
    print("Request received2")
    return json.dumps({"status": True})

if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
