from PyQt5 import QtCore, QtGui, QtWidgets


class TableWindow(QtWidgets.QWidget):

    def __init__(self, data: list[str] = None, headers: list[str] = None, parent=None):
        super(TableWindow, self).__init__(parent)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.headers = headers
        self.data = data
        self.setup_ui()
        self.__fill_table()

    def setup_ui(self):
        self.setObjectName("self")
        self.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Table window"))

    def __fill_table(self):
        if self.data is not None and self.headers is not None:
            self.tableWidget.clear()
            rows_count = len(self.data)
            column_count = len(self.headers)
            self.tableWidget.setRowCount(rows_count)
            self.tableWidget.setColumnCount(column_count)
            self.tableWidget.setHorizontalHeaderLabels(self.headers)
            for row_number, row_data in enumerate(self.data):
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TableWindow()
    ui.show()
    sys.exit(app.exec_())
