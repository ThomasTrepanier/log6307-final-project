from flask import Flask, request
import json
import time
import os
from concurrent.futures import ThreadPoolExecutor


app = Flask(__name__)


# Task manager executor
_threadpool_cpus = int(os.cpu_count() / 2)
EXECUTOR = ThreadPoolExecutor(max_workers=max(_threadpool_cpus, 2))


@app.route("/first", methods=["POST"])
def main():
    print("Request received")
    EXECUTOR.submit(func1)
    return json.dumps({"status": True})


def func1():
    time.sleep(2)
    print("Print function executed")


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
