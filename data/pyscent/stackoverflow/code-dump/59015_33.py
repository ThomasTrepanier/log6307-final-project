from PyQt6 import QtCore, QtGui, QtWidgets
from test_ui import Ui_Window
import resources

class Window(QtWidgets.QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':

    app = QtWidgets.QApplication(['Test'])
    window = Window()
    window.show()
    app.exec()
