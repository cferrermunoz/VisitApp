from PyQt5 import QtCore, QtGui, QtWidgets
from rol import Ui_MainWindow as Ui_Rol
from ExceptionDialog import ExceptionDialog
from PacientWindow import PacientWindow
from MetgeWindow import MetgeWindow

class RolWindow(QtWidgets.QMainWindow,Ui_Rol):
    def __init__(self, parent, db, user, *args, **kwargs):
        super(RolWindow, self).__init__(*args, **kwargs)
        self.setupUi(parent)
        self.parent = parent
        self.db = db
        self.user = user
        self.btnPacient.clicked.connect(self.onClickbtnPacient)
        self.btnMetge.clicked.connect(self.onClickbtnMetge)

    def onClickbtnPacient(self):
        self.close()
        self.parent.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = PacientWindow(self.window, self.db, self.user)
        self.window.show()
        self.hide()

    def onClickbtnMetge(self):
        self.close()
        self.parent.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = MetgeWindow(self.window, self.db, self.user)
        self.window.show()
        self.hide()