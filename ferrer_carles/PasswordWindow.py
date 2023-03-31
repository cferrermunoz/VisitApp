from PyQt5 import QtWidgets
from password import Ui_MainWindow as Ui_Password
from ExceptionDialog import ExceptionDialog
from RolWindow import RolWindow
from PacientWindow import PacientWindow
from MetgeWindow import MetgeWindow


class PasswordWindow(QtWidgets.QMainWindow,Ui_Password):
    def __init__(self, parent, db, user, *args, **kwargs):
        super(PasswordWindow, self).__init__(*args, **kwargs)
        self.setupUi(parent)
        self.db = db
        self.user = user
        self.btnLoginP.clicked.connect(self.btnLogin)
        self.txbPass.returnPressed.connect(self.btnLogin)

    def btnLogin(self):
        self.password = self.txbPass.text()
        if (self.password != self.user["password"]):
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Error")
            dlg.txbExcept.setText("Contraseña incorrecta")
            dlg.exec()
        else:
            metge = self.db.METGES.find_one({'_id': self.user["_id"]})
            pacient = self.db.PACIENTS.find_one({'_id': self.user["_id"]})
            if (metge != None and pacient != None):
                self.hide()
                self.window = QtWidgets.QMainWindow()
                self.ui = RolWindow(self.window, self.db, self.user)
                self.window.show()
                self.hide()
            elif (metge != None):
                self.hide()
                self.window = QtWidgets.QMainWindow()
                self.ui = MetgeWindow(self.window, self.db, self.user)
                self.window.show()
                self.hide()
            else:
                self.hide()
                self.window = QtWidgets.QMainWindow()
                self.ui = PacientWindow(self.window, self.db, self.user)
                self.window.show()
                self.hide()