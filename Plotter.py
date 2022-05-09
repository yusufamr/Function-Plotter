# from curses.ascii import isdigit
from lib2to3.pgen2.literals import evalString
from re import X
from tkinter import Y
from PyQt5 import QtCore, QtGui, QtWidgets 
import numpy as np
from matplotlib.figure import Figure
from pyqtgraph import PlotWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # MainWindow = QtWidgets.QMainWindow()
        self._main = QtWidgets.QWidget()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 720, 365))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setBackground('w')
        self.TE_function = QtWidgets.QTextEdit(self.centralwidget)
        self.TE_function.setGeometry(QtCore.QRect(70, 400, 671, 21))
        self.TE_function.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TE_function.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TE_function.setObjectName("TE_function")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5, 400, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.TE_xMin = QtWidgets.QTextEdit(self.centralwidget)
        self.TE_xMin.setGeometry(QtCore.QRect(70, 430, 111, 21))
        self.TE_xMin.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TE_xMin.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.TE_xMin.setProperty("X_min", 0)
        self.TE_xMin.setObjectName("TE_xMin")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 430, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(575, 430, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.TE_xMax = QtWidgets.QTextEdit(self.centralwidget)
        self.TE_xMax.setGeometry(QtCore.QRect(630, 430, 111, 21))
        self.TE_xMax.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TE_xMax.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.TE_xMax.setProperty("X_min", 0)
        self.TE_xMax.setObjectName("TE_xMax")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(330, 460, 111, 31))
        self.SubmitButton.setIconSize(QtCore.QSize(20, 16))
        self.SubmitButton.setObjectName("SubmitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.SubmitButton.clicked.connect(self.clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Function Plotter"))
        self.TE_function.setPlaceholderText(_translate("MainWindow", "Enter a Function of x"))
        self.label.setText(_translate("MainWindow", "Function :"))
        self.TE_xMin.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "X min"))
        self.label_3.setText(_translate("MainWindow", "X max"))
        self.TE_xMax.setPlaceholderText(_translate("MainWindow", "0"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))

    # Clicked is the function run when user enter the Function and X min & max  
    def clicked(self):
        # check if user enter the Function and X min and X max properly 
        if self.FunctionCheck() and self.checkMinMax(self.TE_xMin.toPlainText(),"Min") and self.checkMinMax(self.TE_xMax.toPlainText(),"Max"):
            Eq = self.TE_function.toPlainText()
            Eq = Eq.replace('^','**') # replace ^ to ** to be power 
            if(float(self.TE_xMin.toPlainText())>float(self.TE_xMax.toPlainText())):
                self.ErrorMsg("xMin cannot be greater than xMax ")
            x=np.arange(float(self.TE_xMin.toPlainText()),float(self.TE_xMax.toPlainText()),0.1) # enter X as a range 
            self.graphicsView.clear()
            # Put plot in a try and except because if there is any other error we didn't handle an error msg will show 
            try:
                 plt = self.graphicsView.plot(x,eval(Eq), title="theTitle", pen='r')
            except:
                self.ErrorMsg("Error in Function, Please enter Function Properly")
    # Function to Pop an error Msg
    def ErrorMsg(self,msg):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.setWindowTitle("Error")
        error_dialog.showMessage(msg)
        error_dialog.exec_()
    # Function to check upon Function that user input it 
    def FunctionCheck(self):
        # check if user didn't enter the function
        if not self.TE_function.toPlainText():
            self.ErrorMsg("Function cannot be empty")
            return False
        else:
            #then check if user enter any operator or variable that isn't in our scope
            for i in self.TE_function.toPlainText():
                if i.isdigit() or i==' ' or i == 'x' or i == 'X' or i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
                    continue
                self.ErrorMsg("You have entered an unsupported varible or operator.Function must be variable of x, and the operator are: * / - + ^")
                return False
        return True
    # check if user enter Min and Max properly
    def checkMinMax(self,msg,type):
        #if user didn't enter the Min or Max
        if not msg :
            self.ErrorMsg("Enter the %s value"%(type))
            return False
        else:
            #check if user enter Min and Max as digits or not
            try:
                float(msg)
            except:
                self.ErrorMsg("The %s value have to be a number"%(type))
                return False
        return True



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.show()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())
