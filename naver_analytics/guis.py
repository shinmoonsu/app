def setHeader(self, header):
	# print(header[0])
	tableFields = [ x['name'] for x in header["data"] ]
	
	self.tableWidget.setColumnCount(len(header["data"]))
	self.tableWidget.setHorizontalHeaderLabels(tableFields)
	self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: %s}" % header['background']);
	self.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section {background-color: %s}" % header['background']);
	for k in range(0,len(header["data"])):
		self.tableWidget.horizontalHeader().resizeSection(k, header["data"][k]['width'])
	self.tableWidget.setAlternatingRowColors(True)