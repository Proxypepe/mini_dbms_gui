from PyQt5 import QtCore, QtGui, QtWidgets
from src.core.completer import SQLDictionaryCompleter


class ReadPage(QtWidgets.QWidget):

    def __init__(self):
        super(ReadPage, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("self")
        self.resize(642, 281)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_current = QtWidgets.QPushButton(self)
        self.show_current.setMaximumSize(QtCore.QSize(130, 16777215))
        self.show_current.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_current.setObjectName("show_current")
        self.verticalLayout.addWidget(self.show_current)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setCompleter(SQLDictionaryCompleter())
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.execute_btn = QtWidgets.QPushButton(self)
        self.execute_btn.setMinimumSize(QtCore.QSize(120, 0))
        self.execute_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.execute_btn.setObjectName("execute_btn")
        self.horizontalLayout.addWidget(self.execute_btn)
        self.show_btn = QtWidgets.QPushButton(self)
        self.show_btn.setMinimumSize(QtCore.QSize(120, 0))
        self.show_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_btn.setObjectName("show_btn")
        self.horizontalLayout.addWidget(self.show_btn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.execute_btn.setText(_translate("self", "Execute"))
        self.show_btn.setText(_translate("self", "Show in window"))
        self.show_current.setText(_translate("self", "Show current table"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.QWidget()
    ui = ReadPage()
    ui.show()
    sys.exit(app.exec_())
