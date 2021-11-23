from PyQt5 import QtCore, QtGui, QtWidgets

from src.db.repository import Repository
from src.views.read_page import ReadPage
from src.views.table_window import TableWindow


class ReadFrameController:
    def __init__(self, view: ReadPage, repository: Repository):
        self.view = view
        self.repository = repository
        self.current_table = ""

        self.rows = None

        self.data = []
        self.headers = []

        self.view.show_current.clicked.connect(self.show_current_table)
        self.view.execute_btn.clicked.connect(self.execute)
        self.view.show_btn.clicked.connect(self.show_window)

    def show_current_table(self):
        query = f"SELECT * FROM {self.current_table};"
        self.rows = self.repository.execute(query)  # move to __fill_table
        self.__fill_table(self.rows)

    def execute(self):
        if self.view.lineEdit.text() != "":
            query = self.view.lineEdit.text()
            self.rows = self.repository.execute(query)
            self.__fill_table(self.rows)
            self.view.lineEdit.clear()

    def show_window(self):
        self.window = TableWindow(self.data, self.headers)
        self.window.show()

    def __fill_table(self, rows):
        if rows is not None:
            descriptions = rows.cursor.description
            headers = [description[0] for description in descriptions]
            self.headers = headers
            rows_count = rows.rowcount
            column_count = len(descriptions)
            self.view.tableWidget.setRowCount(rows_count)
            self.view.tableWidget.setColumnCount(column_count)
            self.view.tableWidget.setHorizontalHeaderLabels(headers)
            tmp = []
            self.data.clear()
            for row_number, row_data in enumerate(rows):
                for column_number, data in enumerate(row_data):
                    tmp.append(str(data))
                    self.view.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.data.append(tmp.copy())
                tmp.clear()
