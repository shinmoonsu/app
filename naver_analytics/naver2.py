import sys,requests,re,time,datetime
import threading,json

import naver_ui
from guis import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2 import QtCore
from PySide2.QtGui import *
from xlwt import Workbook

def setConnect(self):
	self.connect(self.tableWidget,QtCore.SIGNAL("continu_state(QString)"), self.continu_state)
	self.lineEdit.returnPressed.connect(self.ok_handler)
	self.lineEdit.textChanged.connect(self.textChk)
	self.pushButton.clicked.connect(self.ok_handler)
	self.actionExit.triggered.connect(self.exit)
	self.actionSAVE_EXCEL.triggered.connect(self.excel)

class Form(QMainWindow, naver_ui.Ui_MainWindow): 
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		self.setupUi(self)
		fpath = "F:\\sublime\\내부서버-shin-관리ftp\\응용프로그램\\naver_analytics\\naverShopAdCategorySearch.json"

		with open(fpath,encoding='UTF8') as f:
			schema = json.load(f)

		setHeader(self, schema['header'])
		setConnect(self)
		self.statusbar.showMessage("Ready")
		self.lineEdit.setFocus()


	def textChk(self):
		text = self.lineEdit.text()
		text = re.sub("\n",",",text)
		self.lineEdit.setText(text)
		

	def continu_state(self,keyword):
		self.statusbar.showMessage("%s 검색중" % keyword)

	def exit(self):
		self.close()

	def excel(self):
		xdir = QFileDialog.getSaveFileName(self, u"저장경로","네이버쇼핑 카테고리 및 광고 검색_"+datetime.datetime.now().strftime('%Y%m%d%H%M%S'),"*.xls")
		xdir = xdir[0]
		if xdir:
			wb = Workbook()

			ws = wb.add_sheet("검색결과")
			row_count = self.tableWidget.rowCount()
			col_count = self.tableWidget.columnCount()
			for y in range(col_count):
				a = self.tableWidget.horizontalHeaderItem(y).text()
				ws.write(0, y, a)
			
			for x in range(row_count):
				for y in range(col_count):
					try:
						a = self.tableWidget.item(x,y).text()
						ws.write(x+1, y, a)
					except AttributeError:
						ws.write(x+1, y, "")

		wb.save(xdir)
		del wb
		QMessageBox.warning(self,'저장완료','엑셀파일이 저장되었습니다.')

	def ok_handler(self):
		keyword = self.lineEdit.text()
		keywords = keyword.split(",")
		self.tableWidget.setRowCount(len(keywords))
		i=0
		for keyword in keywords:
			rt = threading.Thread(target=self.search,args=(keyword, i)).start()
			i+=1	

	def search(self, keyword, i):
		self.tableWidget.emit(SIGNAL("continu_state(QString)"), keyword)
		self.tableWidget.setItem( i,0,QTableWidgetItem(str(keyword)))
		rt = requests.get("https://search.shopping.naver.com/search/all.nhn?where=all&frm=NVSCTAB&query=%s" % keyword)
		rt = rt.text
		try:
			val = re.compile('"price">(.*?)</s.*?"depth">(.*?)</s', re.DOTALL).findall(rt)
			c1 = re.compile("<a.*?>(.*?)</a>", re.DOTALL).findall(val[0][0])
			c2 = re.compile("<a.*?>(.*?)</a>", re.DOTALL).findall(val[0][1])
			if len(c1)==0:
				c1 = ['']
			self.tableWidget.setItem( i,2,QTableWidgetItem(str(c1[0])))
			self.tableWidget.setItem( i,3,QTableWidgetItem(str("/".join(c2))))
			# print(self.tableWidget.takeItem(i,1).text)
		except:
			pass
		self.tableWidget.setItem( i,1,QTableWidgetItem(str("완료"))) 


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = Form()
	ui.show()
	sys.exit(app.exec_())