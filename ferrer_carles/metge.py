# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metge.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txbUser = QtWidgets.QLabel(self.centralwidget)
        self.txbUser.setObjectName("txbUser")
        self.gridLayout_2.addWidget(self.txbUser, 0, 1, 1, 1)
        self.btnTancarSessio = QtWidgets.QPushButton(self.centralwidget)
        self.btnTancarSessio.setObjectName("btnTancarSessio")
        self.gridLayout_2.addWidget(self.btnTancarSessio, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout.setObjectName("gridLayout")
        self.twVProg = QtWidgets.QTableWidget(self.tab_1)
        self.twVProg.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twVProg.setObjectName("twVProg")
        self.twVProg.setColumnCount(0)
        self.twVProg.setRowCount(0)
        self.gridLayout.addWidget(self.twVProg, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnEdit = QtWidgets.QPushButton(self.tab_1)
        self.btnEdit.setObjectName("btnEdit")
        self.gridLayout.addWidget(self.btnEdit, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(9, 9, 171, 21))
        self.label_6.setObjectName("label_6")
        self.twVPass = QtWidgets.QTableWidget(self.tab_2)
        self.twVPass.setGeometry(QtCore.QRect(9, 44, 751, 441))
        self.twVPass.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twVPass.setObjectName("twVPass")
        self.twVPass.setColumnCount(0)
        self.twVPass.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(False)
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.lblPacient = QtWidgets.QLabel(self.tab_3)
        self.lblPacient.setObjectName("lblPacient")
        self.gridLayout_3.addWidget(self.lblPacient, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.lblHora = QtWidgets.QLabel(self.tab_3)
        self.lblHora.setObjectName("lblHora")
        self.gridLayout_3.addWidget(self.lblHora, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)
        self.btnCancel = QtWidgets.QPushButton(self.tab_3)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout_3.addWidget(self.btnCancel, 5, 0, 1, 1)
        self.btnDesar = QtWidgets.QPushButton(self.tab_3)
        self.btnDesar.setObjectName("btnDesar")
        self.gridLayout_3.addWidget(self.btnDesar, 5, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_3.addWidget(self.plainTextEdit, 4, 0, 1, 2)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txbUser.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">TextLabel</span></p></body></html>"))
        self.btnTancarSessio.setText(_translate("MainWindow", "Tancar sessió"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Usuari:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Visites programades</span></p></body></html>"))
        self.btnEdit.setText(_translate("MainWindow", "Editar visita"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Visites Programades"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Visites Passades</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Visites Passades"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Pacient:</span></p></body></html>"))
        self.lblPacient.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">TextLabel</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Hora:</span></p></body></html>"))
        self.lblHora.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">TextLabel</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Realitzada:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Informe:</span></p></body></html>"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel·lar"))
        self.btnDesar.setText(_translate("MainWindow", "Desar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Visita actual"))
