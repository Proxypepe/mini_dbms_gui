from PyQt5 import QtCore, QtGui, QtWidgets


class UpdateField(QtWidgets.QWidget):
    def __init__(self):
        super(UpdateField, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("self")
        self.resize(560, 90)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.field_box_2 = QtWidgets.QComboBox(self)
        self.field_box_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.field_box_2.setMinimumSize(QtCore.QSize(150, 0))
        self.field_box_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.field_box_2.setObjectName("field_box_2")
        self.horizontalLayout.addWidget(self.field_box_2)
        self.new_value_le_2 = QtWidgets.QLineEdit(self)
        self.new_value_le_2.setObjectName("new_value_le_2")
        self.horizontalLayout.addWidget(self.new_value_le_2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UpdateField()
    ui.setup_ui()
    ui.show()
    sys.exit(app.exec_())
