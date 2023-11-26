import threading
from multiprocessing import Queue

class CSVWriterThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.input_queue = Queue()

    def send(self, item):
        self.input_queue.put(item)

    def close(self):
        self.input_queue.put(None)
        self.input_queue.join()

    def run(self):
        while True:
            csv_array = self.input_queue.get()
            if csv_array is None:
                break

            # Do something here ...
            df = pd.DataFrame({'x': csv_array})
            df.to_csv("docs/xyz.csv", index=False)


            self.input_queue.task_done()
            time.sleep(1)
        # Done
        self.input_queue.task_done()
        return

@app.before_first_request
def activate_job_monitor():
    thread = CSVWriterThread()
    app.csvwriter = thread
    thread.start()
