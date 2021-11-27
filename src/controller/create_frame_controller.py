from src.views.create_page import CreatePage
from src.db.repository import Repository

from src.views.create_field import CreateField


class CreateFrameController:
    def __init__(self, view: CreatePage, repository: Repository):
        self.view = view
        self.repository = repository
        self.current_table = ""
        self.fields: list[CreateField] = []
        self._validate_data = None
        self.view.create_btn.clicked.connect(self.insert)

    def add_fields(self, fields):
        for field in self.fields:
            field.setVisible(False)
            self.view.verticalLayout.removeWidget(field)
        self.fields.clear()

        for field, _type in fields:
            if self.current_table.lower()[:-2] in field.lower():
                continue
            create_field = CreateField()
            create_field.field_name_lbl.setText(field)
            create_field.type_lbl.setText(_type)
            self.view.verticalLayout.addWidget(create_field)
            self.fields.append(create_field)

    def clear_fields(self):
        for field in self.fields:
            field.value_le.clear()

    def validate(self) -> bool:
        pass

    def insert(self):
        query = f"INSERT INTO {self.current_table}"
        columns = []
        values = []
        for field in self.fields:
            if field.value_le.text() == "":
                return
            type_text = field.type_lbl.text()
            if type_text in ("date", "varchar"):
                values.append(f"'{field.value_le.text()}'")
            else:
                values.append(field.value_le.text())
            columns.append(field.field_name_lbl.text())
        columns_str = ", ".join(columns)
        values_str = ", ".join(values)
        query = f"{query} ({columns_str}) VALUES ({values_str});"
        self.repository.execute(query)
        self.clear_fields()

    @property
    def validate_data(self):
        return self._validate_data

    @validate_data.setter
    def validate_data(self, data_types):
        self._validate_data = data_types
