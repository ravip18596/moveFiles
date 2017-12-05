from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import shutil
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 387)
        MainWindow.setFixedSize(MainWindow.size())
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.130864, y1:0.131, x2:0.92, y2:0.903409, stop:0 rgba(59, 227, 209, 255), stop:1 rgba(255, 255, 255, 255));")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 171, 51))
        self.pushButton.setStyleSheet("font: 75 12pt \"Calibri\";\n"
"color: rgb(0, 0, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 60, 201, 51))
        self.pushButton_2.setStyleSheet("font: 75 12pt \"Calibri\";\n"
"color: rgb(170, 0, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 142, 141, 81))
        self.pushButton_3.setStyleSheet("font: 75 italic 24pt \"Calibri\";\n"
"background-color: rgb(85, 255, 127);\n"
"color: rgb(170, 0, 127);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 142, 141, 81))
        self.pushButton_4.setStyleSheet("font: 75 italic 24pt \"Calibri\";\n"
"background-color: rgb(85, 255, 127);\n"
"color: rgb(170, 0, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        


        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(57, 282, 331, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.srcdir)
        self.pushButton_2.clicked.connect(self.destdir)
        self.pushButton_3.clicked.connect(self.move)
        self.pushButton_4.clicked.connect(self.copy)

    def srcdir(self):
        dialog = QtWidgets.QFileDialog()
        self.src = dialog.getExistingDirectory(None, "Select Folder")
        if self.src=="":
        	QMessageBox.about(self, "Error", "Please specify source directory")
        
            
    def destdir(self):
        dialog = QtWidgets.QFileDialog()
        self.dest = dialog.getExistingDirectory(None, "Select Folder")
        if self.dest=="":
        	QMessageBox.about(self, "Error", "Please specify source directory")
        

    def move(self):
        if os.path.exits(self.src):
            files = os.listdir(self.src)
        else:
            QMessageBox.about(self, "Error", "Please specify source directory")
        xt = "/Moved_files"
        if not os.path.exits(os.path.join(self.dest,xt)):
            os.makedirs(os.path.join(self.dest,xt))
        cnt,tot = 1, len(files)
        self.completed=0
        for f in files:
            self.completed = (cnt*100/tot)
            shutil.move(self.src + "/" + f, self.dest+"/Moved_files/")
            self.progressBar.setValue(self.completed)
            cnt += 1
    
    def copy(self):
        files1 = os.listdir(self.src)
        os.makedirs(self.dest+"/Copied_files")
        cnt1,tot1 = 1, len(files1)
        self.completed=0
        for f in files1:
            self.completed = (cnt1*100/tot1)
            shutil.copy(self.src + "/" + f, self.dest+"/Copied_files/")
            self.progressBar.setValue(self.completed)
            cnt1 += 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Select Source directory"))
        self.pushButton_2.setText(_translate("MainWindow", "Select Destination directory"))
        self.pushButton_3.setText(_translate("MainWindow", "Move"))
        self.pushButton_4.setText(_translate("MainWindow","Copy"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

















