from PyQt5 import QtCore, QtGui, QtWidgets

from src.views.update_page import UpdatePage
from src.views.update_field import UpdateField
from src.db.repository import Repository


class UpdateController:
    def __init__(self, view: UpdatePage, repository: Repository) -> None:
        self._current_table = ""
        self.fields = []
        self.repository = repository
        self.view = view
        self.view.add_field_btn.clicked.connect(self.add_field)
        self.view.update_btn.clicked.connect(self.validate)
        self.fields.append(self.view.widget)

    def add_field(self):
        widget = UpdateField()
        self.fields.append(widget)
        self.view.verticalLayout.addWidget(widget)

    def validate(self):
        for field in self.fields:
            print(field.new_value_le_2.text())

    @property
    def current_table(self):
        return self._current_table

    @current_table.setter
    def current_table(self, table_name):
        self._current_table = table_name
