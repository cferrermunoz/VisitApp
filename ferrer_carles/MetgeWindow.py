from PyQt5 import QtWidgets
from metge import Ui_MainWindow as Ui_Metge
import datetime
from ExceptionDialog import ExceptionDialog
from ConfirmDialog import ConfirmDialog

class MetgeWindow(QtWidgets.QMainWindow,Ui_Metge):
    def __init__(self, parent, db, user, *args, **kwargs):
        super(MetgeWindow, self).__init__(*args, **kwargs)
        self.setupUi(parent)
        self.parent = parent
        self.db = db
        self.user = user
        self.llistaMetges = []
        for x in self.db.METGES.find():
            y = self.db.USUARIS.find_one({'_id': x["_id"]}, {'login': 1, 'Cognoms_i_Nom': 1})
            self.llistaMetges.append(y)
        # Init window
        self.txbUser.setText(self.user["login"])
        self.comboBox.addItem("Selecciona una opció")
        self.comboBox.addItem("Sí")
        self.comboBox.addItem("No")
        # Connect signals
        self.btnTancarSessio.clicked.connect(self.onClickbtnTancarSessio)
        self.twVProg.cellClicked.connect(self.onClicktwVProg)
        self.twVPass.cellClicked.connect(self.onClicktwVPass)
        self.comboBox.currentIndexChanged.connect(self.onChangedcomboBox)
        self.btnDesar.clicked.connect(self.onClickbtnDesar)
        self.btnCancel.clicked.connect(self.onClickbtnCancel)
        # Init tables
        self.twVProg.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twVPass.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.init_twVProg()
        self.init_twVPass()

    def onClickbtnDesar(self):
        text = self.plainTextEdit.toPlainText()
        print(text)
    def onClickbtnCancel(self):
        self.comboBox.setCurrentIndex(0)
        self.plainTextEdit.clear()
    def onChangedcomboBox(self):
        self.btnDesar.setEnabled(False)
        self.btnCancel.setEnabled(False)
        if self.comboBox.currentIndex() != 0:
            self.btnDesar.setEnabled(True)
            self.btnCancel.setEnabled(True)
    def onClicktwVProg(self):
        if self.twVProg.currentRow() != -1:
            print("ok")
    def onClicktwVPass(self):
        if self.twVPass.currentRow() != -1:
            print("ok")
    def init_twVPass(self):
        self.twVPass.setColumnCount(4)
        self.twVPass.setHorizontalHeaderLabels(["Data", "Hora", "Pacient", "Realitzada"])
        self.twVPass.setRowCount(0)
        self.twVPass.setColumnWidth(0, 100)
        self.twVPass.setColumnWidth(1, 100)
        self.twVPass.setColumnWidth(2, 200)
        for x in self.db.METGES.find({"_id": self.user["_id"]}):
            for y in x['agenda']:
                if y['id_pacient'] != 0:
                    if y['moment_visita'] < datetime.datetime.today():
                        self.twVPass.insertRow(self.twVPass.rowCount())
                        self.twVPass.setItem(self.twVPass.rowCount() - 1, 0,
                                             QtWidgets.QTableWidgetItem(y['moment_visita'].strftime("%d/%m/%Y")))
                        self.twVPass.setItem(self.twVPass.rowCount() - 1, 1,
                                             QtWidgets.QTableWidgetItem(y['moment_visita'].strftime("%H:%M")))
                        self.twVPass.setItem(self.twVPass.rowCount() - 1, 2,
                                             QtWidgets.QTableWidgetItem(self.db.USUARIS.find_one({"_id": y['id_pacient']})['Cognoms_i_Nom']))
                        self.twVPass.setItem(self.twVPass.rowCount() - 1, 3,
                                             QtWidgets.QTableWidgetItem(y['realitzada']))
    def init_twVProg(self):
        self.twVProg.setColumnCount(3)
        self.twVProg.setHorizontalHeaderLabels(["Data", "Hora", "Pacient"])
        self.twVProg.setRowCount(0)
        self.twVProg.setColumnWidth(0, 100)
        self.twVProg.setColumnWidth(1, 100)
        self.twVProg.setColumnWidth(2, 200)
        for x in self.db.METGES.find({"_id": self.user["_id"]}):
            for y in x['agenda']:
                if y['id_pacient'] != 0:
                    if y['moment_visita'] > datetime.datetime.today():
                        self.twVProg.insertRow(self.twVProg.rowCount())
                        self.twVProg.setItem(self.twVProg.rowCount()-1, 0, QtWidgets.QTableWidgetItem(y['moment_visita'].strftime("%d/%m/%Y")))
                        self.twVPass.setItem(self.twVPass.rowCount() - 1, 1,
                                             QtWidgets.QTableWidgetItem(y['moment_visita'].strftime("%H:%M")))
                        self.twVPass.setItem(self.twVPass.rowCount() - 1, 2,
                                             QtWidgets.QTableWidgetItem(
                                                 self.db.USUARIS.find_one({"_id": y['id_pacient']})['Cognoms_i_Nom']))
    def onClickbtnTancarSessio(self):
        self.parent.close()
