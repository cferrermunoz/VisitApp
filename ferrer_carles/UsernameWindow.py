import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from PasswordWindow import PasswordWindow
from NoPasswordWindow import NoPasswordWindow
from ExceptionDialog import ExceptionDialog
from username import Ui_MainWindow

class UsernameWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnLogin.clicked.connect(self.onClickBtnLogin)
        self.txbUsername.returnPressed.connect(self.onClickBtnLogin)
        try:
            load_dotenv()
            mongodb = os.getenv("mongodb")
            user = os.getenv("user")
            password = os.getenv("password")
            client = MongoClient("mongodb+srv://" + user + ":" + password + mongodb)
        except:
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Error")
            dlg.txbExcept.setText("No se pudo cargar los datos de los ficheros de conexión")
            dlg.exec()
        try:
            self.db = client.cferrer1
            self.db.USUARIS.find_one({'login': 'xagueda'})
        except:
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Error")
            dlg.txbExcept.setText("No se pudo conectar con la base de datos")
            dlg.exec()

    def onClickBtnLogin (self):
        self.login = self.txbUsername.text()
        self.user = self.db.USUARIS.find_one({"login": self.login}, { 'login': 1, 'password': 1})
        print(self.user)
        if(self.user == None):
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Error")
            dlg.txbExcept.setText("Usuario no encontrado")
            dlg.exec()
            return
        if(self.user["password"] == ""):
            # paldana
            self.window = QtWidgets.QMainWindow()
            self.ui = NoPasswordWindow(self.window, self.db, self.user)
            self.ui.txbUser.setText(self.login)
            self.window.show()
            self.hide()
        else:
            # xagueda
            self.window = QtWidgets.QMainWindow()
            self.ui = PasswordWindow(self.window, self.db, self.user)
            self.ui.txbUser.setText(self.login)
            self.window.show()
            self.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UsernameWindow()
    window.show()
    sys.exit(app.exec_())