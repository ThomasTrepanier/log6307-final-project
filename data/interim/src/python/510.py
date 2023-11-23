class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # Setup window size.
        self.resize(800, 600)  # Width, height in pixels.

        # Center the window on the screen.
        screen_geometry = QDesktopWidget().screenGeometry()
        window_geometry = self.geometry()
        self.move(
            (screen_geometry.width() - window_geometry.width()) / 2,
            (screen_geometry.height() - window_geometry.height()) / 2
        )
