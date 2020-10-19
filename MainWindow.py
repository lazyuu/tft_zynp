# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(621, 40)
        MainWindow.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QPushButton{\n"
"    color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"    border: 2px solid qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));   \n"
"    background-color: rgb(22,26,32);\n"
"    ridge:ridge;\n"
"    padding: 4px;\n"
"    border-radius:10px;\n"
"    \n"
"    font: 75 14pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));   \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
" \n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_zdlb = QtWidgets.QPushButton(self.centralwidget)
        self.bt_zdlb.setObjectName("bt_zdlb")
        self.horizontalLayout.addWidget(self.bt_zdlb)
        self.bt_gfzr = QtWidgets.QPushButton(self.centralwidget)
        self.bt_gfzr.setEnabled(True)
        self.bt_gfzr.setAutoDefault(False)
        self.bt_gfzr.setDefault(False)
        self.bt_gfzr.setFlat(False)
        self.bt_gfzr.setObjectName("bt_gfzr")
        self.horizontalLayout.addWidget(self.bt_gfzr)
        self.bt_yx = QtWidgets.QPushButton(self.centralwidget)
        self.bt_yx.setEnabled(True)
        self.bt_yx.setAutoDefault(False)
        self.bt_yx.setDefault(False)
        self.bt_yx.setFlat(False)
        self.bt_yx.setObjectName("bt_yx")
        self.horizontalLayout.addWidget(self.bt_yx)
        self.bt_zb = QtWidgets.QPushButton(self.centralwidget)
        self.bt_zb.setEnabled(True)
        self.bt_zb.setAutoDefault(False)
        self.bt_zb.setDefault(False)
        self.bt_zb.setFlat(False)
        self.bt_zb.setObjectName("bt_zb")
        self.horizontalLayout.addWidget(self.bt_zb)
        self.bt_ds = QtWidgets.QPushButton(self.centralwidget)
        self.bt_ds.setObjectName("bt_ds")
        self.horizontalLayout.addWidget(self.bt_ds)
        self.bt_gb = QtWidgets.QPushButton(self.centralwidget)
        self.bt_gb.setEnabled(True)
        self.bt_gb.setAutoDefault(False)
        self.bt_gb.setDefault(False)
        self.bt_gb.setFlat(False)
        self.bt_gb.setObjectName("bt_gb")
        self.horizontalLayout.addWidget(self.bt_gb)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_zdlb.setText(_translate("MainWindow", "自动列表"))
        self.bt_gfzr.setText(_translate("MainWindow", "官方阵容"))
        self.bt_yx.setText(_translate("MainWindow", "英雄"))
        self.bt_zb.setText(_translate("MainWindow", "装备"))
        self.bt_ds.setText(_translate("MainWindow", "打赏"))
        self.bt_gb.setText(_translate("MainWindow", "关闭"))
