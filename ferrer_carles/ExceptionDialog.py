from PyQt5 import QtWidgets
from exception import Ui_Dialog

class ExceptionDialog(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(ExceptionDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)