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
        self.txbUser.setText(self.user["login"])

    def onClickbtnConfirm(self):
        dlg = ConfirmDialog()
        dlg.setWindowTitle("Confirmar Reserva")
        # dlg.txbMetge.setText("Metge: " + self.txbMetge.text())
        # dlg.txbDatetime.setText("Fecha: " + self.txbDatetime.text())
        dlg.exec()
