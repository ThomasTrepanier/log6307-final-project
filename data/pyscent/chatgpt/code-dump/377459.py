class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # Setup window size.
        self.resize(800, 600)  # Width, height in pixels.

        # Setup window initial location.
        self.move(300, 200)  # X, Y position in pixels.
