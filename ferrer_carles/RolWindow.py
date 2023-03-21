from PyQt5 import QtCore, QtGui, QtWidgets
from rol import Ui_MainWindow as Ui_Rol
from ExceptionDialog import ExceptionDialog

class RolWindow(QtWidgets.QMainWindow,Ui_Rol):
    def __init__(self, parent, db, user, *args, **kwargs):
        super(RolWindow, self).__init__(*args, **kwargs)
        self.setupUi(parent)
        self.db = db
        self.user = user
        self.btnPacient.clicked.connect(self.onClickbtnPacient)
        self.btnMetge.clicked.connect(self.onClickbtnMetge)

    def onClickbtnPacient(self):
        print("Pacient")

    def onClickbtnMetge(self):
        print("Metge")