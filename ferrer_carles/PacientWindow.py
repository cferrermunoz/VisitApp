from PyQt5 import QtWidgets
from pacient import Ui_MainWindow as Ui_Pacient
from ExceptionDialog import ExceptionDialog
from ConfirmDialog import ConfirmDialog

class PacientWindow(QtWidgets.QMainWindow,Ui_Pacient):
    def __init__(self, parent, db, user, *args, **kwargs):
        super(PacientWindow, self).__init__(*args, **kwargs)
        self.setupUi(parent)
        self.db = db
        self.user = user
        self.btnConfirm.clicked.connect(self.onClickbtnConfirm)
        self.txbUser.setText(self.user["login"])
        self.calendarWidget.clicked.connect(self.onClickCalendar)
        llistaEsp = []
        for x in self.db.METGES.find():
            if x['especialitat'] not in llistaEsp:
                llistaEsp.append(x['especialitat'])
        llistaEsp.append("Totes")
        for x in llistaEsp:
            self.cboEspecialitat.addItem(x)
        self.cboEspecialitat.setCurrentIndex(len(llistaEsp)-1)
        for x in self.db.METGES.find():
            y = self.db.USUARIS.find_one({'_id': x["_id"]}, {'login': 1, 'nom': 1, 'cognom1': 1, 'cognom2': 1})
            self.cboMetge.addItem(y["nom"] + " " + y["cognom1"] + " " + y["cognom2"])

    def onClickbtnConfirm(self):
        dlg = ConfirmDialog()
        dlg.setWindowTitle("Confirmar Reserva")
        # dlg.txbMetge.setText("Metge: " + self.txbMetge.text())
        # dlg.txbDatetime.setText("Fecha: " + self.txbDatetime.text())
        dlg.exec()

    def onClickCalendar(self):
        print(self.calendarWidget.selectedDate().toString("dd/MM/yyyy"))
        self.dateEdit.setDate(self.calendarWidget.selectedDate())
