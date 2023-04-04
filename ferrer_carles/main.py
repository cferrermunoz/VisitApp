import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from UsernameWindow import UsernameWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.window = QtWidgets.QMainWindow()
        self.ui = UsernameWindow(None)
        self.ui.show()
        self.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.hide()
    sys.exit(app.exec_())