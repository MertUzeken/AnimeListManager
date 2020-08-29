# -*- coding: utf-8 -*-
# Author: Mert Uzeken
# Project Name: Anime List Manager
# Form implementation generated from reading ui file 'form.ui'
# Created by: PyQt5 UI code generator 5.13.2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
from pop_loader import Loader
import os

class QCustomQWidget (QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(QCustomQWidget, self).__init__(parent)
        #Create the container and add widgets such as label into it by using add.Widget()
        #ToDo: set a maximum size to the label to keep the thumbnail size uniform
        self.container = QtWidgets.QVBoxLayout() #<---- Container (QV = Vertical)
        self.namelabel = QtWidgets.QLabel()      #<---- Label goes into the Container
        self.container.addWidget(self.namelabel) #<---- Added label into the Container by addWidget()
        self.box       = QtWidgets.QHBoxLayout() #<---- Adds another Container (QH = Horizontal)
        self.iconlabel = QtWidgets.QLabel()      #<---- Adds a label into the QH box
        self.box.addWidget(self.iconlabel, 0)    #<---- Gives the layout positioning
        self.box.addLayout(self.container, 1)    #<---- Positions the
        self.setLayout(self.box)
        self.namelabel.setStyleSheet('''
            color: rgb(66, 66, 66);
        ''')

    def setName(self,text):
        self.namelabel.setText(text)

    def setIcon(self, imagePath):
        self.iconlabel.setPixmap(QtGui.QPixmap(imagePath))

    def defaultIcon(self):
        self.iconlabel.setPixmap(QtGui.QPixmap("noimg.png"))


class Ui_Form(Loader):
    def searchAction(self):
        print("")
        #Search the list for specific titles ...

    def addItemAction(self):
        print("")
        #Add to list

    def deleteItemAction(self):
        print("")
        #Delete from local list

    def switchListAction(self):
        print("")
        #Switch between lists

    def prefmenu(self):
        print("")
        #Preferences

    def switchLists(self):
        directory = os.path.dirname(__file__)+"/thumbnails/"
        titles = self.titleReader()
        counter=0
        for element in titles[1:]:
            counter+=1
            title = str(element[0])
            self.myCustomWidget = QCustomQWidget()                                   # Create Custom Widget
            self.myCustomWidget.setName(title)                                       # Set Titles
            self.myCustomWidget.setIcon(directory+str(counter)+".jpg")               # Set Thumbnails
            myQListWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)           # Create QListWidgetItem
            myQListWidgetItem.setSizeHint(self.myCustomWidget.sizeHint())            # Set size hint (?)
            self.listWidget.addItem(myQListWidgetItem)                               # AddQListWidgetItem into QListWidget
            self.listWidget.setItemWidget(myQListWidgetItem, self.myCustomWidget)    # Put it into the "Container"

    def setupUi(self, Form):
        InterfaceIcons = os.path.dirname(__file__)+"/Icons/"

        Form.setObjectName("Form")
        Form.resize(762, 539)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(762, 539))
        Form.setMaximumSize(QtCore.QSize(762, 539))
        Form.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 50, 82, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.Pref_Button = QtWidgets.QPushButton(self.frame)
        self.Pref_Button.setGeometry(QtCore.QRect(5, 430, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Pref_Button.setFont(font)
        self.Pref_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(InterfaceIcons + "switchnew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pref_Button.setIcon(icon)
        self.Pref_Button.setIconSize(QtCore.QSize(35, 35))
        self.Pref_Button.setFlat(True)
        self.Pref_Button.setObjectName("Pref_Button")
        self.Pref_Button.clicked.connect(self.prefmenu)

        self.Switchlist_button = QtWidgets.QPushButton(self.frame)
        self.Switchlist_button.setGeometry(QtCore.QRect(5, 20, 71, 41))
        self.Switchlist_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(InterfaceIcons + "menunew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Switchlist_button.setIcon(icon1)
        self.Switchlist_button.setIconSize(QtCore.QSize(35, 35))
        self.Switchlist_button.setFlat(True)
        self.Switchlist_button.setObjectName("Switchlist_button")
        self.Switchlist_button.clicked.connect(self.switchListAction)

        self.Add_Button = QtWidgets.QPushButton(self.frame)
        self.Add_Button.setGeometry(QtCore.QRect(5, 80, 71, 41))
        self.Add_Button.setFlat(True)
        self.Add_Button.setObjectName("Add_Button")
        self.Add_Button.clicked.connect(self.addItemAction)

        self.Delete_Button = QtWidgets.QPushButton(self.frame)
        self.Delete_Button.setGeometry(QtCore.QRect(5, 140, 71, 41))
        self.Delete_Button.setFlat(True)
        self.Delete_Button.setObjectName("Delete_Button")
        self.Delete_Button.clicked.connect(self.deleteItemAction)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(664, 17, 87, 28))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(InterfaceIcons + "search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(22, 22))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.searchAction)

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(89, 17, 572, 28))
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setMaxLength(25)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(90, 50, 661, 481))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(1)
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setObjectName("listWidget")
        self.switchLists()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Anime List Manager"))
        self.Add_Button.setText(_translate("Form", "Add"))
        self.Delete_Button.setText(_translate("Form", "Delete"))
        self.pushButton.setText(_translate("Form", "Search"))
        self.lineEdit.setPlaceholderText(_translate("Form", " Search . . ."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
