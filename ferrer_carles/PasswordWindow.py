from PyQt5 import QtWidgets
from password import Ui_MainWindow as Ui_Password
from ExceptionDialog import ExceptionDialog
from RolWindow import RolWindow

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
            print("Contraseña correcta")
            self.window = QtWidgets.QMainWindow()
            self.ui = RolWindow(self.window, self.db, self.user)
            self.window.show()
            self.hide()
