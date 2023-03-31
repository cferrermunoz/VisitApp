from PyQt5 import QtWidgets
from pacient import Ui_MainWindow as Ui_Pacient
from ConfirmDialog import ConfirmDialog
from datetime import datetime


class PacientWindow(QtWidgets.QMainWindow,Ui_Pacient):
    def __init__(self, parent, db, user, *args, **kwargs):
        super(PacientWindow, self).__init__(*args, **kwargs)
        self.setupUi(parent)
        self.parent = parent
        self.db = db
        self.user = user
        self.calendarWidget.setSelectedDate(datetime.today())
        self.dateEdit.setDate(datetime.today())
        # self.btnTancarSessio.clicked.connect(self.onClickbtnTancarSessio)
        self.btnConfirm.clicked.connect(self.onClickbtnConfirm)
        self.txbUser.setText(self.user["login"])
        self.calendarWidget.clicked.connect(self.onClickCalendar)
        self.cboHora.addItem("Selecciona una hora")
        self.cboHora.addItem("09:00")
        self.cboHora.addItem("09:30")
        llistaEsp = []
        for x in self.db.METGES.find():
            if x['especialitat'] not in llistaEsp:
                llistaEsp.append(x['especialitat'])
        llistaEsp.append("Totes")
        for x in llistaEsp:
            self.cboEspecialitat.addItem(x)
        self.cboEspecialitat.setCurrentIndex(len(llistaEsp)-1)
        self.cboHora.currentIndexChanged.connect(self.onClickCboHora)
        for x in self.db.METGES.find():
            y = self.db.USUARIS.find_one({'_id': x["_id"]}, {'login': 1, 'nom': 1, 'cognom1': 1, 'cognom2': 1})
            self.cboMetge.addItem(y["nom"] + " " + y["cognom1"] + " " + y["cognom2"])

    # def onClickbtnTancarSessio(self):
    #     self.close()
    #     self.parent.close()
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = UsernameWindow(None)
    #     self.window.show()
    #     self.hide()
    def onClickCboHora(self):
        if (self.cboHora.currentIndex() != 0):
            self.btnConfirm.setEnabled(True)
        else:
            self.btnConfirm.setEnabled(False)
    def onClickbtnConfirm(self):
        dlg = ConfirmDialog()
        dlg.setWindowTitle("Confirmar Reserva")
        dlg.txbMetge.setText("Metge: " + self.cboMetge.currentText())
        # dlg.txbDatetime.setText("Fecha: " + self.txbDatetime.text())
        dlg.exec()

    def onClickCalendar(self):
        self.dateEdit.setDate(self.calendarWidget.selectedDate())
