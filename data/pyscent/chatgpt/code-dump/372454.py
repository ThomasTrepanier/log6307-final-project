from PyQt5.QtWidgets import QMessageBox

class BookSearchApp(QWidget):
    # ...

    def on_bibtex_button_click(self):
        if not self.current_book:
            return

        bibtext = self.generate_bibtext(self.current_book)
        with open('citation.bib', 'w') as f:
            f.write(bibtext)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("BibTeX citation has been saved to citation.bib")
        msg.setWindowTitle("Download Complete")
        msg.exec_()
