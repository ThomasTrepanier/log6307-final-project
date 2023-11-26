def run_together(*functions):
    processes = []
    for function in functions:
        process = Process(target=function)
        process.start()
        processes.append(process)
    for process in processes:
        process.join()

@app.route("/first", methods=["POST"])
def main():
    print("Request received")

    return run_together(func1, func2)

def func1():
    time.sleep(100)
    print("Print function executed")

def func2():
    return json.dumps({"status": True})
