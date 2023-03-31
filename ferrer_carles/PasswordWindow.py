from PyQt5 import QtWidgets
from password import Ui_MainWindow as Ui_Password
from ExceptionDialog import ExceptionDialog
from RolWindow import RolWindow
from PacientWindow import PacientWindow
from MetgeWindow import MetgeWindow
import hashlib


class PasswordWindow(QtWidgets.QMainWindow,Ui_Password):
    def __init__(self, parent, db, user, *args, **kwargs):
        super().__init__(parent)


        self.setupUi(parent)
        self.parent = parent
        self.db = db
        self.user = user
        self.btnLoginP.clicked.connect(self.onClickbtnLogin)
        self.txbPass.returnPressed.connect(self.onClickbtnLogin)
        self.btnCancel.clicked.connect(self.onClickBtnCancel)

    def onClickBtnCancel (self):
        self.close()
    def onClickbtnLogin(self):
        password = self.txbPass.text()
        password = hashlib.sha1(password.encode('utf-8')).hexdigest()
        if (password != self.user["password"]):
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Error")
            dlg.txbExcept.setText("Contraseña incorrecta")
            dlg.exec()
        else:
            metge = self.db.METGES.find_one({'_id': self.user["_id"]})
            pacient = self.db.PACIENTS.find_one({'_id': self.user["_id"]})
            if (metge != None and pacient != None):
                self.close()
                self.parent.close()
                self.window = QtWidgets.QMainWindow()
                self.ui = RolWindow(self.window, self.db, self.user)
                self.window.show()
                self.hide()
            elif (metge != None):
                self.close()
                self.parent.close()
                self.window = QtWidgets.QMainWindow()
                self.ui = MetgeWindow(self.window, self.db, self.user)
                self.window.show()
                self.hide()
            else:
                self.close()
                self.parent.close()
                self.window = QtWidgets.QMainWindow()
                self.ui = PacientWindow(self.window, self.db, self.user)
                self.window.show()
                self.hide()