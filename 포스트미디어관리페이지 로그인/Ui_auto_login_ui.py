# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\sublime\내부서버-shin-관리ftp\응용프로그램\포스트미디어관리페이지 로그인\auto_login_ui.ui',
# licensing of 'f:\sublime\내부서버-shin-관리ftp\응용프로그램\포스트미디어관리페이지 로그인\auto_login_ui.ui' applies.
#
# Created: Tue Aug  7 10:45:46 2018
#      by: pyside2-uic  running on PySide2 5.11.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(260, 441)
        mainWindow.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 241, 421))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtWidgets.QApplication.translate("mainWindow", "관리계정 자동로그인", None, -1))

