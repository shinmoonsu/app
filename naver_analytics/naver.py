import sys,requests,re
import threading

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2 import QtCore
from PySide2.QtGui import *


class TableModel(QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        QAbstractTableModel.__init__(self, *args, **kwargs)
        self.values = [[0,0,0]]

    def columnCount(self, parent=QModelIndex()):
        return len(self.values[0])

    def rowCount(self, parent=QModelIndex()):
        return len(self.values)

    def data(self, index, role=Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount() and 0 <= index.column() < self.columnCount():
            if role == Qt.DisplayRole:
                return self.values[index.row()][index.column()]

class Form(QObject): 
	def __init__(self, ui_file, parent=None):
		super(Form, self).__init__(parent)
		ui_file = QFile(ui_file)
		ui_file.open(QFile.ReadOnly)

		loader = QUiLoader()
		self.window = loader.load(ui_file)
		ui_file.close()
		self.stat = self.window.findChild(QStatusBar, 'statusbar')
		self.stat.showMessage("Ready")
		self.table = self.window.findChild(QTableWidget, 'tableWidget')

		self.tableFields = ["검색어","광고진행여부","검색카테고리"]
		self.table.setColumnCount(len(self.tableFields))
		self.table.setHorizontalHeaderLabels(self.tableFields)
		self.table.horizontalHeader().resizeSection(1, 80)
		self.table.horizontalHeader().resizeSection(2, 200)
		self.table.setStyleSheet("font: 9pt \"맑은 고딕\";")
		self.table.setFrameShape(QFrame.StyledPanel)
		self.table.setFrameShadow(QFrame.Plain)
		self.table.setLineWidth(10)
		self.table.setMidLineWidth(6)
		self.table.setDragEnabled(True)
		self.table.setAlternatingRowColors(True)
		self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.table.setTextElideMode(Qt.ElideRight)
		self.table.setShowGrid(True)
		self.table.setGridStyle(Qt.CustomDashLine)
		self.table.setWordWrap(True)
		# self.model = TableModel()
		# self.table.setModel(self.model)
		self.line = self.window.findChild(QLineEdit, 'lineEdit')
		self.line.setText("청바지,반바지,레깅스,쫄바지,티셔츠,코트,장화,부츠,운동화")
		self.btn = self.window.findChild(QPushButton, 'pushButton')
		self.btn.clicked.connect(self.ok_handler)
		# QMainWindow.setStatusBar()showMessage(tr("Ready"));
		self.window.show()

	def addRow(self, keyword):
		self.table.setItem(0,1,QTableWidgetItem(str(keyword)))

	def search(self, keyword, i):
		print(i)
		# self.table.insertRow(self.table.rowCount()+1)
		self.table.setItem( i,0,QTableWidgetItem(str(keyword)))
		# self.stat.showMessage("%s 검색중입니다.." % keyword)

		# print(keyword)
		rt = requests.get("https://search.shopping.naver.com/search/all.nhn?where=all&frm=NVSCTAB&query=%s" % keyword)
		rt = rt.text
		try:
			val = re.compile('<span class="price">(.*?)</span>.*?<span class="depth">(.*?)</span>', re.DOTALL).findall(rt)
			c1 = re.compile("<a.*?>(.*?)</a>", re.DOTALL).findall(val[0][0])
			c2 = re.compile("<a.*?>(.*?)</a>", re.DOTALL).findall(val[0][1])
			self.table.setItem( i,1,QTableWidgetItem(str(c1[0])))
			self.table.setItem( i,2,QTableWidgetItem(str("/".join(c2))))
		except:
			pass
		
		# self.model.values.append([keyword, ad, "/".join(xr)])
		
		# self.model.values.append([keyword, ad, "/".join(xr)])
		# self.window.show()
		
		# self.btn.setText("분석시작")

	def ok_handler(self):
		self.btn.setText("분석중")
		keyword = self.line.text()
		keywords = keyword.split(",")
		r = self.table.rowCount()
		c = self.table.columnCount()
		for x in range(0,r):
			for xx in range(0,c):
				self.table.setItem( x,xx,QTableWidgetItem(str("")))
		i=0
		for keyword in keywords:
			threading.Thread(target=self.search,args=(keyword, i)).start()
			i+=1
			
					

 
if __name__ == '__main__':
	print(11)
	app = QApplication()
	# form = Form('%smainwindow.ui' % re.sub("naver.py","", sys.argv[0]))
	print(1)
	form = Form('F:\\sublime\\내부서버-shin-관리ftp\\응용프로그램\\naver_analytics\\mainwindow.ui')
	print(2)
	sys.exit(app.exec_())