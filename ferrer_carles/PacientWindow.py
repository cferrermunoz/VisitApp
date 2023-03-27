from PyQt5 import QtWidgets
from pacient import Ui_MainWindow as Ui_Pacient
from ExceptionDialog import ExceptionDialog
from ConfirmDialog import ConfirmDialog

class PacientWindow(QtWidgets.QMainWindow,Ui_Pacient):
    def __init__(self, parent, db, user, *args, **kwargs):
        super(PacientWindow, self).__init__(*args, **kwargs)
        self.setupUi(parent)
        self.db = db
        self.user = user
        self.btnConfirm.clicked.connect(self.onClickbtnConfirm)

    def onClickbtnConfirm(self):
        self.window = QtWidgets.QDialog()
        self.ui = ConfirmDialog(self.window, self.db, self.user)
        self.window.show()
        self.hide()
