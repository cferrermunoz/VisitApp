# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pacient.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnTancarSessio = QtWidgets.QPushButton(self.centralwidget)
        self.btnTancarSessio.setObjectName("btnTancarSessio")
        self.gridLayout_2.addWidget(self.btnTancarSessio, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.txbUser = QtWidgets.QLabel(self.centralwidget)
        self.txbUser.setObjectName("txbUser")
        self.gridLayout_2.addWidget(self.txbUser, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout.setObjectName("gridLayout")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_1)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_1)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 2, 0, 1, 11)
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cboMetge = QtWidgets.QComboBox(self.tab_1)
        self.cboMetge.setObjectName("cboMetge")
        self.gridLayout.addWidget(self.cboMetge, 1, 1, 1, 1)
        self.btnBuscar = QtWidgets.QPushButton(self.tab_1)
        self.btnBuscar.setObjectName("btnBuscar")
        self.gridLayout.addWidget(self.btnBuscar, 1, 10, 1, 1)
        self.btnConfirm = QtWidgets.QPushButton(self.tab_1)
        self.btnConfirm.setObjectName("btnConfirm")
        self.gridLayout.addWidget(self.btnConfirm, 3, 10, 1, 1)
        self.txbEspecialitat = QtWidgets.QLineEdit(self.tab_1)
        self.txbEspecialitat.setObjectName("txbEspecialitat")
        self.gridLayout.addWidget(self.txbEspecialitat, 1, 7, 1, 1)
        self.cboHora = QtWidgets.QComboBox(self.tab_1)
        self.cboHora.setObjectName("cboHora")
        self.gridLayout.addWidget(self.cboHora, 1, 5, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.btnTancarSessio.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnTancarSessio.setText(_translate("MainWindow", "Tancar sessió"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Usuari:</span></p></body></html>"))
        self.txbUser.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">TextLabel</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Data:"))
        self.label_7.setText(_translate("MainWindow", "Hora:"))
        self.label_3.setText(_translate("MainWindow", "Especialitat"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Demanar hora</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Metge:"))
        self.btnBuscar.setText(_translate("MainWindow", "Buscar"))
        self.btnConfirm.setText(_translate("MainWindow", "Confirmar Reserva"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Deamanar hora"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Visites Passades</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Visites passades"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Visites Programades"))
