from PyQt5 import QtCore, QtGui, QtWidgets
from src.views.update_page import UpdatePage
from src.views.read_page import ReadPage


class CRUDScreen(QtWidgets.QWidget):
    def __init__(self, parent=None, controller=None):
        super(CRUDScreen, self).__init__(parent)
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("self")
        self.resize(685, 475)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.current_table_box = QtWidgets.QComboBox(self)
        self.current_table_box.setMinimumSize(QtCore.QSize(150, 0))
        self.current_table_box.setObjectName("current_table_box")
        self.horizontalLayout.addWidget(self.current_table_box)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.CRUDPages = QtWidgets.QTabWidget(self)
        self.CRUDPages.setObjectName("CRUDPages")
        self.create_page = QtWidgets.QWidget()
        self.create_page.setObjectName("create_page")
        self.CRUDPages.addTab(self.create_page, "")
        self.update_page = UpdatePage(self)
        self.update_page.setObjectName("update_page")
        self.CRUDPages.addTab(self.update_page, "")
        self.delete_page = QtWidgets.QWidget()
        self.delete_page.setObjectName("delete_page")
        self.CRUDPages.addTab(self.delete_page, "")
        self.read_page = ReadPage()
        self.read_page.setObjectName("read_page")
        self.CRUDPages.addTab(self.read_page, "")
        self.verticalLayout.addWidget(self.CRUDPages)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.back_menu = QtWidgets.QPushButton(self)
        self.back_menu.setMinimumSize(QtCore.QSize(100, 25))
        self.back_menu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.back_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_menu.setCheckable(False)
        self.back_menu.setObjectName("back_menu")
        self.horizontalLayout_2.addWidget(self.back_menu)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi()
        self.CRUDPages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.label.setText(_translate("self", "Current table"))
        self.CRUDPages.setTabText(self.CRUDPages.indexOf(self.create_page), _translate("self", "Create"))
        self.CRUDPages.setTabText(self.CRUDPages.indexOf(self.update_page), _translate("self", "Update"))
        self.CRUDPages.setTabText(self.CRUDPages.indexOf(self.delete_page), _translate("self", "Delete"))
        self.CRUDPages.setTabText(self.CRUDPages.indexOf(self.read_page), _translate("self", "Read"))
        self.back_menu.setText(_translate("self", "Back to menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = CRUDScreen()
    ui.setup_ui()
    ui.show()
    sys.exit(app.exec_())
