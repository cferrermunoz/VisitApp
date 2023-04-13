from PyQt5 import QtWidgets, QtCore, QtGui
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
        self.filtre = {'agenda.id_pacient': self.user['_id']}
        self.llista_visita = self.db.METGES.find(self.filtre)
        self.avui = datetime.today()
        #inicio de la ventana
        self.calendarWidget.setSelectedDate(datetime.today())
        self.dateEdit.setDate(datetime.today())
        self.txbUser.setText(self.user["login"])
        self.dateEdit.setMaximumDateTime(datetime.strptime("2023-06-30", "%Y-%m-%d"))
        self.dateEdit.setMinimumDateTime(datetime.strptime("2023-01-02", "%Y-%m-%d"))
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
        #connects
        self.dateEdit.dateChanged.connect(self.onSelectedDateChanged)
        self.btnTancarSessio.clicked.connect(self.onClickbtnTancarSessio)
        self.btnConfirm.clicked.connect(self.onClickbtnConfirm)
        self.calendarWidget.clicked.connect(self.onClickCalendar)
        self.btnAvui.clicked.connect(self.onClickbtnAvui)
        self.cboHora.currentIndexChanged.connect(self.onClickCboHora)
        self.cboMetge.currentIndexChanged.connect(self.onClickCboMetge)
        self.cboEspecialitat.currentIndexChanged.connect(self.onClickCboEspecialitat)
        self.twVPass.cellClicked.connect(self.onClickTwVPass)
        self.twVProg.cellClicked.connect(self.onClickTwVProg)
        self.btnPuspose.clicked.connect(self.onClickbtnPuspose)
        self.btnCancelVisita.clicked.connect(self.onClickbtnCancelVisita)
        self.twVProg.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twVPass.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # QTableWidget
        self.init_twVPass()
        self.init_twVProg()

    def onClickbtnCancelVisita(self):
        if self.twVProg.currentRow() != -1:
            data = self.twVProg.item(self.twVProg.currentRow(), 1).text()
            data = datetime.strptime(data, '%d/%m/%Y %H:%M')
            filtre = {'agenda.id_pacient': self.user['_id'], 'agenda.moment_visita': data}
            self.db.METGES.update_one(filtre, {'$pull': {'agenda': {'id_pacient': self.user['_id']}}})
            self.twVProg.removeRow(self.twVProg.currentRow())
            self.twVProg.clearSelection()

    def onClickbtnPuspose(self):
        if self.twVProg.currentRow() != -1:
            self.twVProg.removeRow(self.twVProg.currentRow())
            self.btnPuspose.setEnabled(False)
            self.btnCancelVisita.setEnabled(False)
    def onClickTwVPass(self):
        llista_visita = self.db.METGES.find(self.filtre)
        if self.twVPass.currentRow() != -1:
            for x in llista_visita:
                for y in x['agenda']:
                    if y['id_pacient'] == self.user['_id']:
                        if y['moment_visita'].strftime('%d/%m/%Y %H:%M') == self.twVPass.item(self.twVPass.currentRow(), 1).text():
                            if not isinstance(y['informe'], float):
                                self.teVPass.setText(y['informe'])
                            else:
                                self.teVPass.setText("No hi ha informe")
                            break



    def onClickTwVProg(self):
        self.btnPuspose.setEnabled(False)
        self.btnCancelVisita.setEnabled(False)
        llista_visita = self.db.METGES.find(self.filtre)
        if self.twVProg.currentRow() != -1:
            self.btnPuspose.setEnabled(True)
            self.btnCancelVisita.setEnabled(True)
            for x in llista_visita:
                for y in x['agenda']:
                    if y['id_pacient'] == self.user['_id']:
                        if y['moment_visita'].strftime('%d/%m/%Y %H:%M') == self.twVProg.item(self.twVProg.currentRow(), 1).text():
                            if not isinstance(y['informe'], float):
                                self.teVProg.setText(y['informe'])
                            else:
                                self.teVProg.setText("No hi ha informe")
                            break
    def init_twVProg(self):
        for x in self.llista_visita:
            for y in x['agenda']:
                if y['moment_visita'] > self.avui:
                    if y['id_pacient'] == self.user['_id']:
                        self.twVProg.insertRow(self.twVProg.rowCount())
                        for z in self.llistaMetges:
                            if z['_id'] == x['_id']:
                                self.twVProg.setItem(self.twVProg.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(z['Cognoms_i_Nom']))
                                self.twVProg.setItem(self.twVProg.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(y['moment_visita'].strftime('%d/%m/%Y %H:%M')))

    def init_twVPass(self):
        llista_visita = self.db.METGES.find(self.filtre)
        for x in llista_visita:
            for y in x['agenda']:
                if y['moment_visita'] < self.avui:
                    if y['id_pacient'] == self.user['_id']:
                        self.twVPass.insertRow(self.twVPass.rowCount())
                        for z in self.llistaMetges:
                            if z['_id'] == x['_id']:
                                self.twVPass.setItem(self.twVPass.rowCount()-1, 0, QtWidgets.QTableWidgetItem(z['Cognoms_i_Nom']))
                                self.twVPass.setItem(self.twVPass.rowCount()-1, 1, QtWidgets.QTableWidgetItem(y['moment_visita'].strftime('%d/%m/%Y %H:%M')))
                                self.twVPass.setItem(self.twVPass.rowCount()-1, 2, QtWidgets.QTableWidgetItem(y['realitzada']))



    def onClickCboEspecialitat(self):
        self.dateEdit.setEnabled(False)
        self.cboHora.setEnabled(False)
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
        data_seleccionada = self.dateEdit.date().toPyDate()
        data = datetime(data_seleccionada.year, data_seleccionada.month, data_seleccionada.day)
        if (datetime.today() > data):
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Error")
            dlg.txbExcept.setText("No pots demanar hora en el passat")
            dlg.exec_()
        else:
            self.calendarWidget.setSelectedDate(data)
            for x in self.llistaMetges:
                if x['Cognoms_i_Nom'] == self.cboMetge.currentText():
                    horaris = self.db.METGES.find_one({'_id': x["_id"]},{'agenda': 1})
                    for y in horaris['agenda']:
                        if y['moment_visita'].strftime('%Y-%m-%d') == data.strftime('%Y-%m-%d') and y['id_pacient'] == 0:
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
        self.dateEdit.setDate(datetime.today())
        if (self.cboMetge.currentIndex() != 0):
            self.dateEdit.setEnabled(True)
            self.calendarWidget.setEnabled(True)
        else:
            self.dateEdit.setEnabled(False)
            self.calendarWidget.setEnabled(False)
    def onClickbtnAvui(self):
        self.calendarWidget.setSelectedDate(datetime.today())
        self.dateEdit.setDate(datetime.today())
    def onClickbtnTancarSessio(self):
        self.parent.close()
    def onClickCboHora(self):
        if (self.cboHora.currentIndex() != 0):
            self.btnConfirm.setEnabled(True)
        else:
            self.btnConfirm.setEnabled(False)
    def onClickbtnConfirm(self):
        dlg = ConfirmDialog()
        dlg.setWindowTitle("Confirmar Reserva")
        dlg.txbMetge.setText("Metge: " + self.cboMetge.currentText())
        dlg.txbDatetime.setText(self.dateEdit.date().toPyDate().strftime('%d/%m/%Y')+" "+self.cboHora.currentText())
        result = dlg.exec()
        if result == 1:
            text = dlg.txbSymptoms.toPlainText()
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Reservat")
            dlg.txbExcept.setText("Reserva realitzada correctament")
            dlg.exec_()
            id_pacient = self.user["_id"]
            id_metge = ""
            data_sel = self.dateEdit.date().toPyDate()
            data = datetime(data_sel.year, data_sel.month, data_sel.day)
            for x in self.llistaMetges:
                if x['Cognoms_i_Nom'] == self.cboMetge.currentText():
                    id_metge = x["_id"]
                    break
            filtre = {'_id': id_metge, "agenda.moment_visita": datetime.combine(data, datetime.strptime(self.cboHora.currentText(), '%H:%M').time())}
            camp = {"$set": {"agenda.$.id_pacient": id_pacient, 'agenda.$.informe': text}}
            self.db.METGES.update_one(filtre,camp)
            self.cboMetge.setCurrentIndex(0)
            self.btnAvui.click()
        else:
            dlg = ExceptionDialog()
            dlg.setWindowTitle("Cancel·lat")
            dlg.txbExcept.setText("Operació cancel·lada")
            dlg.exec_()

    def onClickCalendar(self):
        self.dateEdit.setDate(self.calendarWidget.selectedDate())
