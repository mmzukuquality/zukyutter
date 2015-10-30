#! /usr/bin/python
# _*_ coding: utf-8 _*_

import MySQLdb
import sys
import time
import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *

Ui_Widget, throwaway = loadUiType('tweet.ui')


#try:
#	connector = MySQLdb.connect(host="192.168.2.1", user="mmzuku", db="Tweet", passwd="ta9ns2uk7um0", charset="utf8")

#except:
connector = MySQLdb.connect(host="localhost", user="", db="Tweet", passwd="", charset="utf8")


#connector = MySQLdb.connect(host="localhost", user="", passwd="", db="Tweet", charset="utf8")

csr = connector.cursor()

class Tweet(Ui_Widget, QWidget):

	def __init__(self):
		super(QWidget, self).__init__()
		self.setupUi(self)
		self.connect(self.Bt, SIGNAL("clicked()"), self, SLOT("update()"))
		self.connect(self.Bt_2, SIGNAL("clicked()"), self, SLOT("reflect()"))

		csr.execute("SELECT Tweet FROM TimeLine ORDER BY Time DESC LIMIT 11")

		rs = str(csr.fetchone())
		rs = rs.lstrip("(u'")
		rs = rs.rstrip(",')")
		self.label.setText(rs)
	
		rs = str(csr.fetchone())
       	        rs = rs.lstrip("(u'")
       	        rs = rs.rstrip(",')")
		self.label_2.setText(rs)
	
		rs =str( csr.fetchone())
		rs = rs.lstrip("(u'")
       	        rs = rs.rstrip(",')")
		self.label_3.setText(rs)
	
		rs = str(csr.fetchone())
		rs = rs.lstrip("(u'")
       	        rs = rs.rstrip(",')")
		self.label_4.setText(rs)

		rs = str(csr.fetchone())
                rs = rs.lstrip("(u'")
                rs = rs.rstrip(",')")
		self.label_5.setText(rs)

		rs = str(csr.fetchone())
                rs = rs.lstrip("(u'")
                rs = rs.rstrip(",')")
		self.label_6.setText(rs)

		rs = str(csr.fetchone())
                rs = rs.lstrip("(u'")
                rs = rs.rstrip(",')")
		self.label_7.setText(rs)

		rs = str(csr.fetchone())
                rs = rs.lstrip("(u'")
                rs = rs.rstrip(",')")
		self.label_8.setText(rs)

		rs = str(csr.fetchone())
                rs = rs.lstrip("(u'")
       		rs = rs.rstrip("',)")
		self.label_9.setText(rs)
	
		rs = str(csr.fetchone())
                rs = rs.lstrip("(u'")
                rs = rs.rstrip("',)'")
		self.label_10.setText(rs)

		rs = str(csr.fetchone())
       	        rs = rs.lstrip("(u'")
               	rs = rs.rstrip("',)")
		self.label_11.setText(rs)

		#time.sleep(30)
		
	@pyqtSlot()
	def reflect(self):
		#try:
		#	connects = MySQLdb.connect(host="192.168.2.1", user="mmzuku", passwd="ta9ns2uk7um0", db="Tweet", charset="utf8")
		#except:
		connects = MySQLdb.connect(host='localhost', user='', passwd='', db='Tweet',charset='utf8')
		
		csr = connects.cursor()
		csr.execute("SELECT Tweet FROM TimeLine ORDER BY Time DESC LIMIT 11")

		tw = str(csr.fetchone())
		tw = tw.lstrip("(u'")
		tw = tw.rstrip(",')")
		self.label.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_2.setText(tw)

		tw =str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_3.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_4.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_5.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_6.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_7.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_8.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip("',)")
		self.label_9.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip("',)")
		self.label_10.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip("',)")
		self.label_11.setText(tw)


	@pyqtSlot()
	def update(self):
		#try:
		#	connects = MySQLdb.connect(host="192.168.2.1", user="mmzuku", passwd="ta9ns2uk7um0", db="Tweet", charset="utf8")
		#except:
		connects = MySQLdb.connect(host='localhost', user='', passwd='', db='Tweet',charset='utf8')
		
		csr = connects.cursor()

		tweet = self.lineEdit.text()
		date = datetime.datetime.today()
		id = "mmzuku"

		data = (id,tweet,date)

		sql = u"insert into TimeLine(ID,Tweet,Time) values(%s,%s,%s)"
		csr.execute(sql,data)

		connects.commit()
		
		self.lineEdit.setText("")

		csr.execute("SELECT Tweet FROM TimeLine ORDER BY Time DESC LIMIT 11")

		tw = str(csr.fetchone())
		tw = tw.lstrip("(u'")
		tw = tw.rstrip(",')")
		self.label.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_2.setText(tw)

		tw =str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_3.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_4.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_5.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_6.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_7.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip(",')")
		self.label_8.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip("',)")
		self.label_9.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip("',)")
		self.label_10.setText(tw)

		tw = str(csr.fetchone())
                tw = tw.lstrip("(u'")
                tw = tw.rstrip("',)")
		self.label_11.setText(tw)


ap = QApplication(sys.argv)

win = Tweet()

win.setWindowTitle('zukyutter')

win.show()

sys.exit(ap.exec_())
