from PyQt5 import QtWidgets
from puspose import Ui_Dialog

class PusposeDialog(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(PusposeDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)