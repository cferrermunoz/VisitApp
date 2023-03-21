from PyQt5 import QtWidgets
from nopassword import Ui_MainWindow as Ui_NoPassword
from ExceptionDialog import ExceptionDialog

class NoPasswordWindow(QtWidgets.QMainWindow,Ui_NoPassword):
    def __init__(self, parent, db, user, *args, **kwargs):
        super(NoPasswordWindow, self).__init__(*args, **kwargs)
        self.setupUi(parent)
        self.db = db
        self.user = user
        self.btnLoginNP.clicked.connect(self.btnChangePass)
        self.txbPass2.returnPressed.connect(self.btnChangePass)

    def btnChangePass(self):
        pass1 = self.txbPass1.text()
        pass2 = self.txbPass2.text()
        print(pass1)
        if (pass2 != pass1):
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Error")
            dlg.txbExcept.setText("Las contraseñas no coinciden")
            dlg.exec()
        else:
            print("Contraseña cambiada")
            print(pass1)
            print(pass2)
            self.db.Usuaris.update_one({"login": self.login}, {"$set": {"password": pass1}})
            print(1)