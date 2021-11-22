from PyQt5 import QtCore, QtGui, QtWidgets


class ExecuteArea(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ExecuteArea, self).__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("self")
        self.resize(695, 475)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.result_btn = QtWidgets.QPushButton(self)
        self.result_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.result_btn.setObjectName("result_btn")
        self.verticalLayout.addWidget(self.result_btn)
        self.execute_btn = QtWidgets.QPushButton(self)
        self.execute_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.execute_btn.setObjectName("execute_btn")
        self.verticalLayout.addWidget(self.execute_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.label.setText("Coding space")
        self.result_btn.setText("See the result")
        self.execute_btn.setText("Execute")

        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ExecuteArea()
    ui.show()
    sys.exit(app.exec_())
