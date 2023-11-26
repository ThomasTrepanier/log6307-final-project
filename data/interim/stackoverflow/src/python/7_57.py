from threading import Thread
from multiprocessing import Process #and multiprocessing queue if you use this
import queue #for passing messages between main and func1

message_queue = queue.Queue()
@app.route("/first", methods=["GET"])
def main():
    print("Request received")
    func_thread = Thread(target=func1, args=(), daemon=True).start() #daemon if it needs to die with main program, otherwise daemon=False
    #or func_process = Process(...) #in case

    return json.dumps({"status": True})

def func1():
    ...
    print("func 1 ")
    message_queue.put(...) #if you need to pass something
    message_queue.get(...) #to get something like stopping signal
    return

