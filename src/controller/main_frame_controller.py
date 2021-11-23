import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject

from src.views.main_frame import MainWindow
from src.db.repository import Repository


class MainWindowController(QObject):

    def __init__(self):
        super(MainWindowController, self).__init__()
        self.repository = Repository.create_repository()
        self.view = MainWindow(self)
        self.__init_window()
        self.execute_page = self.view.page
        self.result_page = self.view.page_2
        self.easy_page = self.view.page_3

        self.execute_page.easy_btn.clicked.connect(self.move_easy_mode)
        self.execute_page.result_btn.clicked.connect(self.show_result)
        self.execute_page.execute_btn.clicked.connect(self.execute)

        self.result_page.get_back_btn.clicked.connect(self.get_back)

        self.easy_page.back_menu.clicked.connect(self.get_back)

    def show_result(self):
        self.view.stackedWidget.setCurrentIndex(1)

    def get_back(self):
        self.view.stackedWidget.setCurrentIndex(0)

    def move_easy_mode(self):
        self.view.stackedWidget.setCurrentIndex(2)

    def execute(self):
        query = self.execute_page.textEdit.toPlainText()
        rows = self.repository.execute(query)
        if rows is not None:
            descriptions = rows.cursor.description
            headers = [description[0] for description in descriptions]
            rows_count = rows.rowcount
            column_count = len(descriptions)
            self.result_page.tableView.setRowCount(rows_count)
            self.result_page.tableView.setColumnCount(column_count)
            self.result_page.tableView.setHorizontalHeaderLabels(headers)
            for row_number, row_data in enumerate(rows):
                for column_number, data in enumerate(row_data):
                    self.result_page.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def get_grud_screen(self):
        return self.easy_page

    def __init_window(self):
        self.view.setup_ui()
        self.view.show()

