from PyQt5 import QtWidgets
from nopassword import Ui_MainWindow as Ui_NoPassword
from ExceptionDialog import ExceptionDialog
from RolWindow import RolWindow
import hashlib
from MetgeWindow import MetgeWindow
from PacientWindow import PacientWindow

class NoPasswordWindow(QtWidgets.QMainWindow,Ui_NoPassword):
    def __init__(self, parent, db, user, *args, **kwargs):
        super().__init__(parent)
        self.setupUi(parent)
        self.parent = parent
        self.db = db
        self.user = user
        self.btnLoginNP.clicked.connect(self.btnChangePass)
        self.txbPass2.returnPressed.connect(self.btnChangePass)

    def btnChangePass(self):
        pass1 = self.txbPass1.text()
        pass2 = self.txbPass2.text()
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
            pass1 = hashlib.sha1(pass1.encode('utf-8')).hexdigest()
            filtre = {"login": self.user["login"]}
            camp = {"$set": {"Password": pass1}}
            self.db.USUARIS.update_one(filtre, camp)
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
