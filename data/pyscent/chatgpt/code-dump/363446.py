import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QTextEdit
from PyQt5.QtCore import Qt
import requests

class BookSearchApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Book Search')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.search_box = QLineEdit()
        self.layout.addWidget(self.search_box)

        self.search_button = QPushButton('Search')
        self.layout.addWidget(self.search_button)

        self.result_list = QListWidget()
        self.layout.addWidget(self.result_list)

        self.description_text = QTextEdit()
        self.layout.addWidget(self.description_text)

        self.search_button.clicked.connect(self.on_search_button_click)
        self.result_list.itemClicked.connect(self.on_list_item_click)

    def on_search_button_click(self):
        query = self.search_box.text()

        params = {'q': query}
        response = requests.get('https://www.googleapis.com/books/v1/volumes', params=params)
        data = response.json()

        self.result_list.clear()

        for item in data['items']:
            title = item['volumeInfo'].get('title', 'No title available')
            authors = ', '.join(item['volumeInfo'].get('authors', ['No authors available']))
            self.result_list.addItem(f'{title} by {authors}')

    def on_list_item_click(self, item):
        query = item.text().split(' by ')[0]

        params = {'q': query}
        response = requests.get('https://www.googleapis.com/books/v1/volumes', params=params)
        data = response.json()

        description = data['items'][0]['volumeInfo'].get('description', 'No description available')

        self.description_text.setPlainText(description)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = BookSearchApp()
    ex.show()

    sys.exit(app.exec_())
