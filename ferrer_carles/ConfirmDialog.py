from PyQt5 import QtWidgets
from confirm import Ui_Dialog

class ConfirmDialog(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(ConfirmDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)