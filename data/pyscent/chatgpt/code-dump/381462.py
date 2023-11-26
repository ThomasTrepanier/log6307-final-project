class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Google Books Search")

        # Set window size
        self.resize(800, 600)

        # Set window position next to dock
        screen_geometry = QDesktopWidget().screenGeometry()
        self.move(50, (screen_geometry.height() - self.height()) / 2) 

        # The rest of your __init__ code...
