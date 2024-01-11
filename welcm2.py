# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcm2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QSize, QCoreApplication, QRect
from PyQt5.QtGui import QPixmap
import random

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy, QFrame

from page import Ui_ThirdWindow
from page2 import Ui_FourthWindow
from Testing import Ui_FifthWindow

class Ui_SecondWindow(object):
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_ThirdWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow2(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_FourthWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FifthWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self,SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(832, 841)
        SecondWindow.setMinimumSize(QtCore.QSize(0, 0))
        SecondWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        SecondWindow.setIconSize(QtCore.QSize(50, 50))


        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)


        self.pracbutton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindow2())
        self.pracbutton.clicked.connect(SecondWindow.close)
        self.pracbutton.setStyleSheet("font: 75 18pt \"Rockwell Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 240, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"font:bold 25px;\n"
"padding:6px;\n"
"min-width:10px;")
        self.pracbutton.setIconSize(QtCore.QSize(18, 18))
        self.pracbutton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pracbutton, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(SecondWindow)
        self.label_3.setObjectName(u"label_2")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("IMG1.jpg"))
        self.label_3.setFixedSize(QSize(500, 260))
        self.label_3.setMaximumSize(QSize(500, 260))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_3.mousePressEvent = self.button_clicked

        self.label = QtWidgets.QLabel(SecondWindow)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 70))
        self.label.setText(QCoreApplication.translate("SecondWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#1e1e1e;\">Categories</span></p></body></html>", None))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindow3())
        self.pushButton_3.clicked.connect(SecondWindow.close)
        self.pushButton_3.setStyleSheet("font: 75 18pt \"Rockwell Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 240, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"font:bold 25px;\n"
"padding:6px;\n"
"min-width:10px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(SecondWindow)
        self.label_4.setObjectName(u"label_2")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("IMG3.jpg"))
        self.label_4.setFixedSize(QSize(500, 260))
        self.label_4.setMaximumSize(QSize(500, 260))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_4.mousePressEvent = self.button_clicked



        self.learnbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.openWindow())
        self.learnbutton.setStyleSheet("font: 75 18pt \"Rockwell Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 240, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"font:bold 25px;\n"
"padding:6px;\n"
"min-width:10px;")
        self.learnbutton.setIconSize(QtCore.QSize(18, 18))
        self.learnbutton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.learnbutton, 1, 1, 1, 1)
        self.learnbutton.clicked.connect(SecondWindow.close)
        self.label_2 = QtWidgets.QLabel(SecondWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("IMG111.jpg"))
        self.label_2.setMaximumSize(QSize(300, 260))
        self.label_2.setFixedSize(QSize(300, 260))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_2.mousePressEvent = self.button_clicked

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        SecondWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)
        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def button_clicked(self, event):
        # Perform button click actions here
        #ui.pracbutton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindow2())
        print("Button clicked!")



    def set_random_image(self):
        images = ["a.jpg", "b.jpg", "c.jpg"]  # Add paths to your images here
        random_image = random.choice(images)
        self.setPixmap(QPixmap(random_image))

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "SecondWindow"))
        self.pracbutton.setText(_translate("MainWindow", "PRACTICE PHASE"))
        self.pushButton_3.setText(_translate("MainWindow", "TESTING PHASE"))
        self.learnbutton.setText(_translate("MainWindow", "LEARNING PHASE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())