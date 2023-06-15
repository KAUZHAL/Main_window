from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QApplication,QScrollBar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from PyQt5.uic import loadUi
class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 827)
        self.centralwidget = QtWidgets.QWidget(MainWindow)#Qwidget is a class of QtWidgets module that passes Mainwindow instance variable  to the instance variable. 
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)#QPushbutton is a  class of  QtWidgets module that passes instance variable as argument to self.pushbutton
        self.pushButton.setGeometry(QtCore.QRect(30,565,400,100))
        font = QtGui.QFont()#creates a new instance of QFont class in QtGUI module and assigns it to font.
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)#sets thickness of font.
        self.pushButton.setFont(font)#sets the font of pusbutton widget to the font specified by 'font' object.
        self.pushButton.setAutoFillBackground(False)#means that pushbutton won't fill its background automatically with the pallete color it finds suitable.
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500,565,400,100))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30,30, 1305,501))
        self.graphicsView.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        self.menuToggle = QtWidgets.QMenu(self.menubar)
        self.menuToggle.setStyleSheet("")
        self.menuToggle.setObjectName("menuToggle")
        self.menuToggleAction = QtWidgets.QAction(MainWindow)
        self.menuToggleAction.setCheckable(True)
        self.menuToggleAction.setObjectName("menuToggleAction")
        self.menuToggle.addAction(self.menuToggleAction)#addAction is a method of QMenu class that passes the argument to menu toggle variable
        self.menubar.addAction(self.menuToggle.menuAction())#action in parenthesis of addAction is to added to menubar
        MainWindow.setMenuBar(self.menubar)#setMenuBar function passes self.menubar to MainWindow instance variable 
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)#function called that is used for translating the features' names 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(1000,565,300, 50))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(300)
        self.horizontalSlider.setValue(300)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.menuToggle.setTitle(_translate("MainWindow", "TOGGLE MODE"))
class MainWindow(QtWidgets.QMainWindow,QScrollBar):
    def __init__(self):
        super().__init__()#calls constructor of superclass to initialize the objects in base class with the logic defined in superclass
        self.ui = Ui_MainWindow()#links object of Ui_Mainwindow to object of Mainwindow.
        self.ui.setupUi(self)#invokes the setupUi() method on self.ui instance by passing self as argument.
        self.ui.menuToggleAction.triggered.connect(self.toggle_dark_bright_mode)
        self.ui.horizontalSlider.valueChanged.connect(self.adjust_size) 
        self.ui.pushButton.clicked.connect(self.start_graph)
        self.ui.pushButton_2.clicked.connect(self.stop_graph)
        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(221)
        self.ax2 = self.fig.add_subplot(222)
        self.ax3 = self.fig.add_subplot(223)
        self.ax4 = self.fig.add_subplot(224)
        self.canvas = FigureCanvas(self.fig)#sets a canvas for plotting
        self.ui.graphicsView.setLayout(QtWidgets.QVBoxLayout())#sets/arranges the positions of widgets vertically in layout 
        self.ui.graphicsView.layout().addWidget(self.canvas)#adds the canvas to the layout
        self.timer = None
        self.data = None
        self.current_index = 0
    def toggle_dark_bright_mode(self,checked):
        if checked:
            self.ui.graphicsView.setBackground('b')
            self.setStyleSheet("QMainWindow { background-color: black; color:white; }")#sets dark mode 
        else:
            self.ui.graphicsView.setBackground('w')
            self.setStyleSheet("QMainWindow { background-color: white; color:black; }")#sets bright mode
    def adjust_size(self, value):
        size = value / 300.0  #normalizes the slider value between 0 and 1
        button_width = int(400 * size)#adjusts the button width based on the slider value
        button_height = int(100 * size)#adjusts the button height based on the slider value
        #for updating the size of the push buttons
        button_font = self.ui.pushButton.font()
        font_size = int(72 * size * 0.7)#adjusts the font size based on the button width
        button_font.setPointSize(font_size)
        self.ui.pushButton.setFont(button_font)
        self.ui.pushButton.setGeometry(QtCore.QRect(30,565, button_width, button_height))
        self.ui.pushButton_2.setFont(button_font)
        self.ui.pushButton_2.setGeometry(QtCore.QRect(500,565, button_width, button_height))
    def start_graph(self):
        if self.data is None:
            self.data = pd.read_csv('C:\\Users\\HP\\New folder\\flightSimulatorResults.csv')
        if self.timer is None or not self.timer.isActive():
            self.timer = QtCore.QTimer()#creates a timer object of class QTimer and passes it to instance variable
            self.timer.timeout.connect(self.update_graph)
            self.timer.start(100)#updates the graph after 0.1 seconds
    def stop_graph(self):
        if self.timer and self.timer.isActive():
            self.timer.stop()
    def update_graph(self):
        x_axis1 = self.data['Time']
        y_axis1 = self.data['Velocity']
        y_axis2 = self.data['Acceleration']
        y_axis3 = self.data['Altitude']
        y_axis4 = self.data['Thrust']
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.ax4.clear()
        self.ax1.plot(x_axis1[:self.current_index+1], y_axis1[:self.current_index+1], 'r-')
        self.ax2.plot(x_axis1[:self.current_index+1], y_axis2[:self.current_index+1], 'b-')
        self.ax3.plot(x_axis1[:self.current_index+1], y_axis3[:self.current_index+1], 'g-')
        self.ax4.plot(x_axis1[:self.current_index+1], y_axis4[:self.current_index+1], 'y-')
        self.ax1.set_xlabel('Time')
        self.ax1.set_ylabel('Velocity')
        self.ax2.set_xlabel('Time')
        self.ax2.set_ylabel('Acceleration')
        self.ax3.set_xlabel('Time')
        self.ax3.set_ylabel('Altitude')
        self.ax4.set_xlabel('Time')
        self.ax4.set_ylabel('Thrust')
        self.canvas.draw()
        self.current_index += 1
        if self.current_index >= len(x_axis1):
            self.current_index = 0
            self.stop_graph()
if __name__ == "__main__":
#In Python, when a script is run, the interpreter sets a special variable called __name__ to the value "__main__" for the script that is being executed. On the other hand, when a module is imported by another script, the __name__ variable is set to the name of that module.
#The line if __name__ == "__main__": is a common idiom used to ensure that a certain block of code is only executed when the script is run directly, and not when it is imported as a module by another script.
    import sys#sys module provides access to system-specific parameters and functions.
    app = QtWidgets.QApplication(sys.argv)#initialization of QApplication object
    window = MainWindow()#creation of Mainwindow
    window.show()
    sys.exit(app.exec_())#starts the event loop(containing UI tasks) and sys.exit() ensures that application exits properly after event loop is terminated.
