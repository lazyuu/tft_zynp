# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_SquadList.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SquadFrom(object):
    def setupUi(self, SquadFrom):
        SquadFrom.setObjectName("SquadFrom")
        SquadFrom.resize(855, 280)
        SquadFrom.setStyleSheet("QTableView\n"
"{\n"
"    font:13px \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"    background: rgba(22,26,32, 200)   \n"
"\n"
"\n"
"}\n"
"QTableView::pane\n"
"{\n"
"    font:13px \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"    \n"
"}\n"
"QScrollBar{\n"
"    background-color:rgb(0, 0, 0);\n"
"    width:10px;\n"
"}\n"
"QScrollBar::handle{\n"
"     image: url(data/img/Center.png)  ; \n"
"     border:none; \n"
"     border-radius:5px;\n"
"} \n"
"QScrollBar::handle:hover{image: url(data/img/Center.png)  ; }\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{background:none;}\n"
"QToolTip{\n"
"border: 2px solid qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));   \n"
"    background-color: rgb(22,26,32);\n"
"    ridge:ridge;\n"
"    padding: 4px;\n"
"    border-radius:10px;\n"
"}\n"
" ")
        self.verticalLayout = QtWidgets.QVBoxLayout(SquadFrom)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabZhengR = QtWidgets.QTableWidget(SquadFrom)
        self.tabZhengR.setObjectName("tabZhengR")
        self.tabZhengR.setColumnCount(11)
        self.tabZhengR.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabZhengR.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        self.tabZhengR.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabZhengR.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabZhengR.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabZhengR.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabZhengR.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabZhengR.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabZhengR.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabZhengR.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabZhengR.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabZhengR.setHorizontalHeaderItem(10, item)
        self.verticalLayout.addWidget(self.tabZhengR)

        self.retranslateUi(SquadFrom)
        QtCore.QMetaObject.connectSlotsByName(SquadFrom)

    def retranslateUi(self, SquadFrom):
        _translate = QtCore.QCoreApplication.translate
        SquadFrom.setWindowTitle(_translate("SquadFrom", "Form"))
        item = self.tabZhengR.horizontalHeaderItem(0)
        item.setText(_translate("SquadFrom", "阵容名称"))
        item = self.tabZhengR.horizontalHeaderItem(1)
        item.setText(_translate("SquadFrom", "强度"))
        item = self.tabZhengR.horizontalHeaderItem(2)
        item.setText(_translate("SquadFrom", "成员1"))
        item = self.tabZhengR.horizontalHeaderItem(3)
        item.setText(_translate("SquadFrom", "成员2"))
        item = self.tabZhengR.horizontalHeaderItem(4)
        item.setText(_translate("SquadFrom", "成员3"))
        item = self.tabZhengR.horizontalHeaderItem(5)
        item.setText(_translate("SquadFrom", "成员4"))
        item = self.tabZhengR.horizontalHeaderItem(6)
        item.setText(_translate("SquadFrom", "成员5"))
        item = self.tabZhengR.horizontalHeaderItem(7)
        item.setText(_translate("SquadFrom", "成员6"))
        item = self.tabZhengR.horizontalHeaderItem(8)
        item.setText(_translate("SquadFrom", "成员7"))
        item = self.tabZhengR.horizontalHeaderItem(9)
        item.setText(_translate("SquadFrom", "成员8"))
        item = self.tabZhengR.horizontalHeaderItem(10)
        item.setText(_translate("SquadFrom", "成员9"))
