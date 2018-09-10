import Ui_auto_login_ui
import sys,requests,re,time,datetime
import threading,json

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

def setConnect(self):
	self.connect(self.tableWidget,QtCore.SIGNAL("continu_state(QString)"), self.continu_state)
	self.lineEdit.returnPressed.connect(self.ok_handler)
	self.lineEdit.textChanged.connect(self.textChk)
	self.pushButton.clicked.connect(self.ok_handler)
	self.actionExit.triggered.connect(self.exit)
	self.actionSAVE_EXCEL.triggered.connect(self.excel)

		
class Form(QMainWindow, Ui_auto_login_ui.Ui_mainWindow): 
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		self.setupUi(self)
		self.treeWidget.setColumnCount(2)
		data = ['발록','사우론','머큐리','간달프','사루만','호빗']
		items = []
		for i in data:
			# print(i)
			items.append(QTreeWidgetItem(None, [i]))

		self.treeWidget.insertTopLevelItems(0, items)
		# _iter = QTreeWidgetItemIterator(self.treeWidget)
		# index = 0
		# while(_iter.value()):
		# 	item = _iter.value()
		# 	# self.treeWidget.assert_(item is items[index])
		# 	index += 1
		# 	_iter += 1




	def exit(self):
		self.close()




if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = Form()
	ui.show()
	sys.exit(app.exec_())