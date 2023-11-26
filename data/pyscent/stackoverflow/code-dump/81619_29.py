msg = QMessageBox()
msg.setIcon(QMessageBox.Icon.Information)

msg.setText('Teste')
msg.setInformativeText("This is additional information")
msg.setWindowTitle("MessageBox demo")
#msg.setDetailedText("The details are as follows:")
msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
msg.buttonClicked.connect(self.msgbtn)
msg.exec()

def msgbtn(self, i):
    print( "Button pressed is:",i.text() )
