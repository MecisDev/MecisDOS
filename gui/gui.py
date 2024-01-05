# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitledswAIml.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1273, 781)
        MainWindow.setMinimumSize(QSize(1273, 781))
        MainWindow.setMaximumSize(QSize(1273, 781))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(0, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1120, 610, 131, 51))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(840, 20, 401, 201))
        font = QFont()
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        self.calendarWidget.setGridVisible(True)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 680, 1281, 61))
        self.line.setCursor(QCursor(Qt.ArrowCursor))
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line.setLineWidth(30)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.browserButton = QPushButton(self.centralwidget)
        self.browserButton.setObjectName(u"browserButton")
        self.browserButton.setGeometry(QRect(10, 693, 75, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1273, 22))
        self.menuFatCisDG = QMenu(self.menubar)
        self.menuFatCisDG.setObjectName(u"menuFatCisDG")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFatCisDG.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">FatCisDG Build 2<br/>05/01/2024</span></p></body></html>", None))
        self.browserButton.setText(QCoreApplication.translate("MainWindow", u"Browser", None))
        self.menuFatCisDG.setTitle(QCoreApplication.translate("MainWindow", u"FatCisDG]", None))
    # retranslateUi

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()   