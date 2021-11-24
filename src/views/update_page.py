from PyQt5 import QtCore, QtGui, QtWidgets
from src.views.update_field import UpdateField


class UpdatePage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UpdatePage, self).__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.resize(678, 341)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.setFont(font)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget = UpdateField()
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
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
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.add_field_btn = QtWidgets.QPushButton(self)
        self.add_field_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_field_btn.setMinimumSize(QtCore.QSize(120, 0))
        self.add_field_btn.setObjectName("add_field_btn")
        self.horizontalLayout_4.addWidget(self.add_field_btn)
        self.update_btn = QtWidgets.QPushButton(self)
        self.update_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.update_btn.setMinimumSize(QtCore.QSize(120, 0))
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout_4.addWidget(self.update_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_2.setText(_translate("self", "Field"))
        self.label_3.setText(_translate("self", "Value"))
        self.label.setText(_translate("self", "Condition"))
        self.comboBox_3.setItemText(0, _translate("self", "="))
        self.comboBox_3.setItemText(1, _translate("self", ">"))
        self.comboBox_3.setItemText(2, _translate("self", "<"))
        self.comboBox_3.setItemText(3, _translate("self", ">="))
        self.comboBox_3.setItemText(4, _translate("self", "<="))
        self.comboBox_3.setItemText(5, _translate("self", "!="))
        self.update_btn.setText(_translate("self", "Update record"))
        self.add_field_btn.setText(_translate("self", "Add field"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UpdatePage()
    ui.show()
    sys.exit(app.exec_())
