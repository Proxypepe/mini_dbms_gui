from PyQt5 import QtCore, QtGui, QtWidgets


class CreateField(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CreateField, self).__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("self")
        self.resize(674, 47)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.field_name_lbl = QtWidgets.QLabel(self)
        self.field_name_lbl.setMinimumSize(QtCore.QSize(120, 0))
        self.field_name_lbl.setObjectName("field_name_lbl")
        self.horizontalLayout.addWidget(self.field_name_lbl)
        self.value_le = QtWidgets.QLineEdit(self)
        self.value_le.setObjectName("value_le")
        self.horizontalLayout.addWidget(self.value_le)
        self.type_lbl = QtWidgets.QLabel(self)
        self.type_lbl.setObjectName("type_lbl")
        self.horizontalLayout.addWidget(self.type_lbl)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.field_name_lbl.setText(_translate("self", "TextLabel"))
        self.type_lbl.setText(_translate("self", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = CreateField()
    ui.show()
    sys.exit(app.exec_())
