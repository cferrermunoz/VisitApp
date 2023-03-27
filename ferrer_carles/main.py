import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from UsernameWindow import UsernameWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UsernameWindow()
    window.show()
    sys.exit(app.exec_())