import sys
from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QCalendarWidget, QFrame, QPushButton, QVBoxLayout, QSplashScreen
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWebEngineWidgets import QWebEngineView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1273, 781)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(0, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(1120, 630, 131, 51)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.setText(u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">FatCisDG Build 1<br/>05/01/2024</span></p></body></html>")
        
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(840, 20, 401, 201)
        self.calendarWidget.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        self.calendarWidget.setGridVisible(True)
        
        self.webEngineView = QWebEngineView(self.centralwidget)  # Assuming QWebEngineView is available
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(10, 20, 471, 641)
        self.webEngineView.setUrl(u"https://vk.com/fatcisdev")
        
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(0, 690, 1281, 61)
        self.line.setCursor(Qt.ArrowCursor)
        self.line.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line.setLineWidth(30)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(950, 300, 271, 111)
        self.pushButton.setText(u"Info")
        self.pushButton.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.show_splash)  # Connect button click to show_splash method

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">FatCisDG Build 1<br/>05/01/2024</span></p></body></html>", None))

    def show_splash(self):
        pixmap = QPixmap(400, 300)
        pixmap.fill(Qt.white)
        splash = QSplashScreen(pixmap)
        splash_font = QFont("Arial", 12)

        text = ("FatCisDos Build 1212\n"
                "FatCisDG Build 1\n"
                "Coded: 05/01/2024\n"
                "FatCisDev 2024")

        splash.setFont(splash_font)
        splash.showMessage(text, Qt.AlignCenter, Qt.black)
        splash.show()

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
