from PyQt5 import QtWidgets
from metge import Ui_MainWindow as Ui_Metge
from ExceptionDialog import ExceptionDialog

class MetgeWindow(QtWidgets.QMainWindow,Ui_Metge):
    def __init__(self, parent, db, user, *args, **kwargs):
        super(MetgeWindow, self).__init__(*args, **kwargs)
        self.setupUi(parent)
        self.db = db
        self.user = user