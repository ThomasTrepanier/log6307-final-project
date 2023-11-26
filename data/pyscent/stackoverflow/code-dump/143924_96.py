def threadingtime_every_sec(sec=60):
    import threading, time
    def loop():
        while True:
            save_datetime()
            time.sleep(sec)
    threading.Thread(target=loop).start()
