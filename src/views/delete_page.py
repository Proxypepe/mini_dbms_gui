from PyQt5 import QtCore, QtGui, QtWidgets


class DeletePage(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(DeletePage, self).__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("self")
        self.resize(642, 280)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.condition_value_2 = QtWidgets.QComboBox(self)
        self.condition_value_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.condition_value_2.setMinimumSize(QtCore.QSize(150, 0))
        self.condition_value_2.setObjectName("condition_value_2")
        self.horizontalLayout_3.addWidget(self.condition_value_2)
        self.comboBox_3 = QtWidgets.QComboBox(self)
        self.comboBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        self.condition_value = QtWidgets.QLineEdit(self)
        self.condition_value.setObjectName("condition_value")
        self.horizontalLayout_3.addWidget(self.condition_value)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.delete_btn = QtWidgets.QPushButton(self)
        self.delete_btn.setMinimumSize(QtCore.QSize(120, 0))
        self.delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.comboBox_3.setItemText(0, _translate("self", "="))
        self.comboBox_3.setItemText(1, _translate("self", ">"))
        self.comboBox_3.setItemText(2, _translate("self", "<"))
        self.comboBox_3.setItemText(3, _translate("self", ">="))
        self.comboBox_3.setItemText(4, _translate("self", "<="))
        self.comboBox_3.setItemText(5, _translate("self", "!="))
        self.delete_btn.setText(_translate("self", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = DeletePage()
    ui.setup_ui()
    ui.show()
    sys.exit(app.exec_())
