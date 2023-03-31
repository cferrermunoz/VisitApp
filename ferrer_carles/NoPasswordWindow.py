from PyQt5 import QtWidgets
from nopassword import Ui_MainWindow as Ui_NoPassword
from ExceptionDialog import ExceptionDialog
from RolWindow import RolWindow
import hashlib

class NoPasswordWindow(QtWidgets.QMainWindow,Ui_NoPassword):
    def __init__(self, parent, db, user, *args, **kwargs):
        super(NoPasswordWindow, self).__init__(*args, **kwargs)
        self.setupUi(parent)
        self.db = db
        self.user = user
        self.btnLoginNP.clicked.connect(self.btnChangePass)
        self.txbPass2.returnPressed.connect(self.btnChangePass)
        self.USUARIS = self.db["USUARIS"]

    def btnChangePass(self):
        pass1 = self.txbPass1.text()
        pass2 = self.txbPass2.text()
        print(pass1)
        if (pass2 != pass1):
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Error")
            dlg.txbExcept.setText("Les contrasenyes no coincideixen")
            dlg.exec()
        else:
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Ok!")
            dlg.txbExcept.setText("Contrasenya creada")
            dlg.exec()
            print(self.user)
            pass1 = hashlib.sha1(pass1.encode('utf-8')).hexdigest()
            filtre = {"login": self.user["login"]}
            camp = {"$set": {"password": pass1}}
            self.USUARIS.update_one(filtre, camp)
            print(pass1)
            self.window = QtWidgets.QMainWindow()
            self.ui = RolWindow(self.window, self.db, self.user)
            self.window.show()
            self.hide()
