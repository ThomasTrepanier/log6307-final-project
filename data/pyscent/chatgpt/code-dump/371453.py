from PyQt5.QtCore import Qt

class BookSearchApp(QWidget):
    # ...

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.on_search_button_click()
        else:
            super().keyPressEvent(event)
