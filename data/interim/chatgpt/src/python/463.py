class BookSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window size
        self.resize(800, 600)

        # Set window position next to dock
        screen_geometry = QDesktopWidget().screenGeometry()
        self.move(50, (screen_geometry.height() - self.height()) / 2)

        self.search_widget = SearchWidget()
        self.setCentralWidget(self.search_widget)

        self.show()
