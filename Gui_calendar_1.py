# gui calendar using Python

from PyQt5 import QtCore, QtGui,QtWidgets

import sys

class UI_MainWindow():
    def setupUI(self,MainWindow):
        # set window title
        MainWindow.resize(501,422)

        # create central widget area on main window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # create calendar widget
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)

        # set geometry for calendar

        self.calendar.setGeometry(QtCore.QRect(0,0,501,371))

        # label to display selected date

        self.label = QtWidgets.QLabel(self.centralwidget)
        # set label geometry
        self.label.setGeometry(QtCore.QRect(5,380,341,31))

        # set label style
        self.label.setStyleSheet('font: 75 22pt Verdana')

        # set label text

        self.label.setText('Select a date')

        # set changed selection

        self.calendar.selectionChanged.connect(self.date)

    def date(self):
        # get selected date
        selected_date = self.calendar.selectedDate()

        # set the label text as selected date

        self.label.setText(str(selected_date.toString()))


# main window 

app = QtWidgets.QApplication(sys.argv)
MainWindow= QtWidgets.QMainWindow()
ui = UI_MainWindow()
ui.setupUI(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
