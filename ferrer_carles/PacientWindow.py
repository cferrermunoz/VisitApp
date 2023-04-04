from PyQt5 import QtWidgets
from pacient import Ui_MainWindow as Ui_Pacient
from ConfirmDialog import ConfirmDialog
from ExceptionDialog import ExceptionDialog
from datetime import datetime


class PacientWindow(QtWidgets.QMainWindow,Ui_Pacient):
    def __init__(self, parent, db, user, *args, **kwargs):
        super(PacientWindow, self).__init__(*args, **kwargs)
        self.setupUi(parent)
        self.parent = parent
        self.db = db
        self.user = user
        #inicio de la ventana
        self.calendarWidget.setSelectedDate(datetime.today())
        self.dateEdit.setDate(datetime.today())
        self.txbUser.setText(self.user["login"])
        self.dateEdit.setMaximumDateTime(datetime.strptime("2023-06-30", "%Y-%m-%d"))
        self.dateEdit.setMinimumDateTime(datetime.strptime("2023-01-02", "%Y-%m-%d"))
        #connects
        self.dateEdit.dateChanged.connect(self.onSelectedDateChanged)
        self.btnTancarSessio.clicked.connect(self.onClickbtnTancarSessio)
        self.btnConfirm.clicked.connect(self.onClickbtnConfirm)
        self.calendarWidget.clicked.connect(self.onClickCalendar)
        self.btnAvui.clicked.connect(self.onClickbtnAvui)
        self.cboHora.currentIndexChanged.connect(self.onClickCboHora)
        self.cboMetge.currentIndexChanged.connect(self.onClickCboMetge)
        self.cboEspecialitat.currentIndexChanged.connect(self.onClickCboEspecialitat)
        #cboEspecialitat
        self.llistaEsp = []
        for x in self.db.METGES.find():
            if x['Especialitat'] not in self.llistaEsp:
                self.llistaEsp.append(x['Especialitat'])
        self.llistaEsp.append("Totes")
        for x in self.llistaEsp:
            self.cboEspecialitat.addItem(x)
        self.cboEspecialitat.setCurrentIndex(len(self.llistaEsp)-1)
        #cboMetge
        self.cboMetge.addItem("Selecciona un metge")
        self.llistaMetges = []
        for x in self.db.METGES.find():
            y = self.db.USUARIS.find_one({'_id': x["_id"]}, {'login': 1, 'Cognoms_i_Nom': 1})
            self.llistaMetges.append(y)
            if y['login'] != self.user['login']:
                self.cboMetge.addItem(y["Cognoms_i_Nom"])
        #cboHora
        self.cboHora.addItem("Selecciona una hora")

    def onClickCboEspecialitat(self):
        self.cboMetge.clear()
        self.cboMetge.addItem("Selecciona un metge")
        if self.cboEspecialitat.currentText() == "Totes":
            for x in self.db.METGES.find():
                y = self.db.USUARIS.find_one({'_id': x["_id"]}, {'login': 1, 'Cognoms_i_Nom': 1})
                if y['login'] != self.user['login']:
                    self.cboMetge.addItem(y["Cognoms_i_Nom"])
        else:
            for x in self.db.METGES.find({'Especialitat': self.cboEspecialitat.currentText()}):
                y = self.db.USUARIS.find_one({'_id': x["_id"]}, {'login': 1, 'Cognoms_i_Nom': 1})
                if y['login'] != self.user['login']:
                    self.cboMetge.addItem(y["Cognoms_i_Nom"])

    def onSelectedDateChanged(self):
        self.cboHora.clear()
        self.cboHora.addItem("Selecciona una hora")
        data = self.dateEdit.date().toPyDate()
        self.calendarWidget.setSelectedDate(data)
        for x in self.llistaMetges:
            if x['Cognoms_i_Nom'] == self.cboMetge.currentText():
                horaris = self.db.METGES.find_one({'_id': x["_id"]},{'agenda': 1})
                for y in horaris['agenda']:
                    if y['moment_visita'].strftime('%Y-%m-%d') == data:
                        print(y['moment_visita'])
                        self.cboHora.addItem(y['moment_visita'].strftime('%H:%M'))
        if self.cboHora.count() == 1:
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Error")
            dlg.txbExcept.setText("No hi ha cap hora disponible per aquest dia")
            dlg.exec_()
        else:
            self.cboHora.setEnabled(True)
            self.cboHora.setCurrentIndex(1)

    def onClickCboMetge(self):
        self.btnConfirm.setEnabled(False)
        if (self.cboMetge.currentIndex() != 0):
            self.dateEdit.setEnabled(True)
        else:
            self.dateEdit.setEnabled(False)
    def onClickbtnAvui(self):
        self.calendarWidget.setSelectedDate(datetime.today())
        self.dateEdit.setDate(datetime.today())
    def onClickbtnTancarSessio(self):
        self.close()
        self.parent.show()
    def onClickCboHora(self):
        if (self.cboHora.currentIndex() != 0):
            self.btnConfirm.setEnabled(True)
        else:
            self.btnConfirm.setEnabled(False)
    def onClickbtnConfirm(self):
        dlg = ConfirmDialog()
        dlg.setWindowTitle("Confirmar Reserva")
        dlg.txbMetge.setText("Metge: " + self.cboMetge.currentText())
        dlg.txbDatetime.setText("Fecha: " + self.dateEdit.date().toPyDate().strftime('%d/%m/%Y') + " Hora: " + self.cboHora.currentText())
        dlg.exec()

    def onClickCalendar(self):
        self.dateEdit.setDate(self.calendarWidget.selectedDate())
