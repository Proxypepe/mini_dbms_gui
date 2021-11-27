from PyQt5 import QtCore, QtGui, QtWidgets

from src.views.update_page import UpdatePage
from src.views.update_field import UpdateField
from src.db.repository import Repository


class UpdateController:
    def __init__(self, view: UpdatePage, repository: Repository) -> None:
        self._current_table = ""
        self._validate_data = None
        self.fields = []
        self.field_names = []
        self.repository = repository
        self.view = view
        self.condition = self.view.condition_value_2
        self.view.add_field_btn.clicked.connect(self.add_field)
        self.view.update_btn.clicked.connect(self.update)
        self.fields.append(self.view.widget)

    def add_field(self):
        widget = UpdateField()
        for field in self.field_names:
            widget.field_box_2.addItem(field)
        self.fields.append(widget)
        self.view.verticalLayout.addWidget(widget)

    def validate(self):
        # TODO Check data types
        changed_fields = []
        for field in self.fields:
            box_text = field.field_box_2.currentText()
            print("box_text: ", box_text)
            print("lbl text: ", field.new_value_le_2.text())
            if box_text in changed_fields:
                return False
            else:
                changed_fields.append(box_text)
            if field.new_value_le_2.text() == "":
                return False
        return False

    def update(self):
        # if self.validate():
        if True:
            query = f"UPDATE {self._current_table} SET "
            args = []
            for field in self.fields:
                box_text = field.field_box_2.currentText()
                value = field.new_value_le_2.text()
                args.append(f"{box_text} = {value}")

            print(f"args {', '.join(args)}")
            query += ', '.join(args) + f" WHERE {self.condition.currentText()} {self.view.comboBox_3.currentText()} " \
                                       f"{self.view.condition_value.text()}"
            self.repository.execute(query)

    def set_boxes(self, fields):
        self.field_names = fields
        for widget_field in self.fields:
            widget_field.field_box_2.clear()
            for field in fields:
                widget_field.field_box_2.addItem(field)

    def set_conditions(self, fields):
        self.view.condition_value_2.clear()
        for field in fields:
            self.view.condition_value_2.addItem(field)

    @property
    def current_table(self):
        return self._current_table

    @current_table.setter
    def current_table(self, table_name):
        self._current_table = table_name

    @property
    def validate_data(self):
        return self._validate_data

    @validate_data.setter
    def validate_data(self, data_types):
        self._validate_data = data_types
