class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # Setup window size.
        self.resize(800, 600)  # Width, height in pixels.

        # Setup window initial location next to the dock.
        screen_geometry = QDesktopWidget().screenGeometry()
        self.move(50, (screen_geometry.height() - self.height()) / 2)  # adjust the 50 based on the width of your dock
