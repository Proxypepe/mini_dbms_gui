from PyQt5 import QtCore, QtGui, QtWidgets

from src.views.execute_area import ExecuteArea
from src.views.result_area import ResultArea
from src.views.crud_frame import CRUDScreen


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, controller=None):
        super(MainWindow, self).__init__()
        self.controller = controller
        self.page_3 = None

    def setup_ui(self):
        self.resize(750, 550)
        self.setWindowTitle("Test")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(self)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)

        self.page = ExecuteArea(self)
        self.stackedWidget.addWidget(self.page)

        self.page_2 = ResultArea(self)
        self.stackedWidget.addWidget(self.page_2)

        self.page_3 = CRUDScreen(self)
        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 25))
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)
    ui = MainWindow()
    ui.setup_ui()
    ui.show()
    sys.exit(app.exec_())
