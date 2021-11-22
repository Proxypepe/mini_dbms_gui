from PyQt5 import QtCore, QtGui, QtWidgets


class ResultArea(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ResultArea, self).__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.resize(685, 475)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.get_back_btn = QtWidgets.QPushButton(self)
        self.get_back_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.get_back_btn.setObjectName("get_back_btn")
        self.horizontalLayout.addWidget(self.get_back_btn)
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableWidget(self)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.get_back_btn.setText(_translate("self", "PushButton"))
        self.label.setText(_translate("self", "Preview space"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ResultArea()
    ui.show()
    sys.exit(app.exec_())
